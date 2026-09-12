import React, { forwardRef } from "react";
import PropTypes from "prop-types";
import { btn, btn_primary, btn_secondary } from "./styles.module.scss";

const variants = { primary: btn_primary, secondary: btn_secondary };

const Button = forwardRef(
  (
    {
      children,
      variant = "primary",
      type = "button",
      disabled = false,
      className = "",
      ...props
    },
    ref
  ) => (
    <button
      ref={ref}
      type={type}
      disabled={disabled}
      className={`${btn} ${variants[variant] || variants.primary} ${className}`}
      {...props}
    >
      {children}
    </button>
  )
);

Button.displayName = "Button";

Button.propTypes = {
  children: PropTypes.node,
  variant: PropTypes.oneOf(["primary", "secondary"]),
  type: PropTypes.string,
  disabled: PropTypes.bool,
  className: PropTypes.string,
};

export default Button;
