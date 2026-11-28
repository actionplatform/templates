import { invoke } from "@tauri-apps/api/core";

export type AppInfo = {
  name: string;
  version: string;
  os: string;
};

export function greet(name: string): Promise<string> {
  return invoke<string>("greet", { name });
}

export function appInfo(): Promise<AppInfo> {
  return invoke<AppInfo>("app_info");
}
