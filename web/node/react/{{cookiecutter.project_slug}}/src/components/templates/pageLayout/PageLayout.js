import React from "react";
import PropTypes from "prop-types";
import { layout } from "./styles.module.scss";

const PageLayout = ({ children }) => <main className={layout}>{children}</main>;

PageLayout.propTypes = { children: PropTypes.node };

export default PageLayout;
