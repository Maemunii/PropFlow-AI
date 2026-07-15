import DashboardIcon from "@mui/icons-material/Dashboard";
import HomeWorkIcon from "@mui/icons-material/HomeWork";
import PeopleIcon from "@mui/icons-material/People";
import AssignmentTurnedInIcon from "@mui/icons-material/AssignmentTurnedIn";
import AssessmentIcon from "@mui/icons-material/Assessment";
import SettingsIcon from "@mui/icons-material/Settings";

import {
  Drawer,
  Toolbar,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
  Divider,
} from "@mui/material";

import { Link, useLocation } from "react-router-dom";

const drawerWidth = 250;

const menu = [
  { text: "Dashboard", icon: <DashboardIcon />, path: "/" },
  { text: "Landlords", icon: <PeopleIcon />, path: "/landlords" },
  { text: "Properties", icon: <HomeWorkIcon />, path: "/properties" },
  { text: "Tasks", icon: <AssignmentTurnedInIcon />, path: "/tasks" },
  { text: "Reports", icon: <AssessmentIcon />, path: "/reports" },
  { text: "Settings", icon: <SettingsIcon />, path: "/settings" },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        "& .MuiDrawer-paper": {
          width: drawerWidth,
          boxSizing: "border-box",
        },
      }}
    >
      <Toolbar>
        <Typography variant="h6" fontWeight="bold">
          🏡 PropFlow AI
        </Typography>
      </Toolbar>

      <Divider />

      <List>
        {menu.map((item) => (
          <ListItemButton
            key={item.text}
            component={Link}
            to={item.path}
            selected={location.pathname === item.path}
          >
            <ListItemIcon>{item.icon}</ListItemIcon>

            <ListItemText primary={item.text} />
          </ListItemButton>
        ))}
      </List>
    </Drawer>
  );
}