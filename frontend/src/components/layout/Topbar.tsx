import NotificationsIcon from "@mui/icons-material/Notifications";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";

import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  IconButton,
} from "@mui/material";

export default function Topbar() {
  return (
    <AppBar
      position="static"
      color="inherit"
      elevation={1}
    >
      <Toolbar>

        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Dashboard
        </Typography>

        <Box>

          <IconButton>
            <NotificationsIcon />
          </IconButton>

          <IconButton>
            <AccountCircleIcon />
          </IconButton>

        </Box>

      </Toolbar>
    </AppBar>
  );
}