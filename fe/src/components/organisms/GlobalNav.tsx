import React from "react";
import { Badge, Divider, Grid, List, ListItemButton, ListItemIcon, ListItemText, Paper, styled, Toolbar } from "@mui/material";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import MuiDrawer from "@mui/material/Drawer";
import IconButton from "@mui/material/IconButton/IconButton";
import PeopleIcon from "@mui/icons-material/People";
import FeedIcon from "@mui/icons-material/Feed";

const drawerWidth: number = 240;
const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== "open" })(({ theme, open }) => ({
  "& .MuiDrawer-paper": {
    position: "relative",
    whiteSpace: "nowrap",
    width: drawerWidth,
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    boxSizing: "border-box",
    ...(!open && {
      overflowX: "hidden",
      transition: theme.transitions.create("width", {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      width: theme.spacing(7),
      [theme.breakpoints.up("sm")]: {
        width: theme.spacing(9),
      },
    }),
  },
}));

type Props = {
  openDrawer: boolean;
  setOpenDrawer: (openDrawer: boolean) => void;
};

type MenuItemProps = {
  label: string;
  icon: JSX.Element;
  href: string;
};

const menuItems: MenuItemProps[] = [
  { label: "Users", icon: <PeopleIcon />, href: "/users" },
  { label: "Articles", icon: <FeedIcon />, href: "/articles" },
];

const GlobalNav = ({ openDrawer, setOpenDrawer }: Props) => {
  return (
    <Drawer variant="permanent" open={openDrawer}>
      <Toolbar
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "flex-end",
          px: [1],
        }}
      >
        <IconButton onClick={() => setOpenDrawer(false)}>
          <ChevronLeftIcon />
        </IconButton>
      </Toolbar>
      <Divider />
      <List component="nav">
        <React.Fragment>
          {menuItems.map((menuItem) => (
            <ListItemButton key={menuItem.label} href={menuItem.href}>
              <ListItemIcon>{menuItem.icon}</ListItemIcon>
              <ListItemText primary={menuItem.label} />
            </ListItemButton>
          ))}
        </React.Fragment>
      </List>
    </Drawer>
  );
};

export default GlobalNav;
