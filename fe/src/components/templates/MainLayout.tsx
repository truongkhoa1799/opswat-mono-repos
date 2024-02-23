import React, { useState } from "react";

import MainHeader, { headerWidth } from "../organisms/MainHeader";
import Box from "@mui/material/Box";

import GlobalNav from "../organisms/GlobalNav";
import { Container } from "@mui/material";

type Props = {
  children: React.ReactNode;
};

const MainLayout = ({ children }: Props): JSX.Element => {
  const [openDrawer, setOpenDrawer] = useState(true);
  return (
    <Box
      component="main"
      overflow="hidden"
      minWidth={0}
      flexGrow={1}
      sx={{
        height: "100vh",
        width: "100%",
        backgroundColor: (theme) => (theme.palette.mode === "light" ? theme.palette.grey[100] : theme.palette.grey[900]),
      }}
    >
      <MainHeader openDrawer={openDrawer} setOpenDrawer={setOpenDrawer} />
      <Box display="flex" flexDirection="row" width="100%">
        <GlobalNav openDrawer={openDrawer} setOpenDrawer={setOpenDrawer} />
        <Container maxWidth="xl" sx={{ mt: 2, mb: 2 }}>
          <Box marginTop={headerWidth} width="100%" height="100vh">
            {children}
          </Box>
        </Container>
      </Box>
    </Box>
  );
};

export default MainLayout;
