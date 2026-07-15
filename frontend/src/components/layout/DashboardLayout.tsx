import { ReactNode } from "react";

import { Box } from "@mui/material";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

interface Props {
  children: ReactNode;
}

export default function DashboardLayout({ children }: Props) {
  return (
    <Box sx={{ display: "flex" }}>
      <Sidebar />

      <Box sx={{ flexGrow: 1 }}>

        <Topbar />

        <Box sx={{ p: 4 }}>
          {children}
        </Box>

      </Box>
    </Box>
  );
}