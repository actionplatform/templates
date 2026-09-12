import { useState, useCallback, useRef, useEffect } from "react";
import axios from "axios";
import api from "./axiosConfig";

const useRequest = (options = {}) => {
  const { onSuccess, onError } = options;
  const onSuccessRef = useRef(onSuccess);
  const onErrorRef = useRef(onError);
  const mountedRef = useRef(true);
  const controllersRef = useRef(new Set());

  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    onSuccessRef.current = onSuccess;
    onErrorRef.current = onError;
  }, [onSuccess, onError]);

  useEffect(() => {
    const controllers = controllersRef.current;
    mountedRef.current = true;
    return () => {
      mountedRef.current = false;
      controllers.forEach((c) => c.abort());
      controllers.clear();
    };
  }, []);

  const execute = useCallback(async (config) => {
    const controller = new AbortController();
    controllersRef.current.add(controller);
    if (mountedRef.current) {
      setLoading(true);
      setError(null);
    }
    try {
      const response = await api({ ...config, signal: controller.signal });
      if (mountedRef.current) setData(response.data);
      const cb = config.onSuccess || onSuccessRef.current;
      if (cb) cb(response.data, response);
      return response.data;
    } catch (err) {
      if (axios.isCancel(err) || err.code === "ERR_CANCELED") return undefined;
      const message =
        err.response?.data?.detail ||
        err.response?.data?.message ||
        err.message ||
        "Request failed";
      if (mountedRef.current) {
        setError(message);
        const cb = config.onError || onErrorRef.current;
        if (cb) cb(err, message);
        throw err;
      }
    } finally {
      controllersRef.current.delete(controller);
      if (mountedRef.current && controllersRef.current.size === 0)
        setLoading(false);
    }
  }, []);

  return { data, error, loading, execute };
};

export default useRequest;
