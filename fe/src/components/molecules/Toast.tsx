import React, { useState } from "react";
import Snackbar from "@mui/material/Snackbar";
import { Alert, AlertTitle } from "@mui/material";

export type ToastProps = {
  severity: "success" | "info" | "warning" | "error";
  message: string;
  isOpen: boolean;
};

const titles = {
  success: "Success",
  info: "Info",
  warning: "Warning",
  error: "Error",
};

const Toast = ({ message, severity, isOpen }: ToastProps) => {
  return (
    <Snackbar anchorOrigin={{ vertical: "top", horizontal: "right" }} open={isOpen} sx={{ width: "300px" }}>
      <Alert severity={severity} sx={{ width: "100%" }}>
        <AlertTitle>{titles[severity]}</AlertTitle>
        {message}
      </Alert>
    </Snackbar>
  );
};

export default Toast;
