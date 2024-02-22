import React from "react";

import Box from "@mui/material/Box";
import { Typography } from "@mui/material";

const PartialError = () => {
  return (
    <Box p="3">
      <Typography variant="h6" component="h6">
        Sorry, an error occurred.
      </Typography>
    </Box>
  );
};

export default PartialError;
