"use client";

import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    text: {
      primary: "#0f172a",
      secondary: "#475569",
    },
  },

  typography: {
    fontFamily: "Geist, sans-serif",

    h4: {
      fontWeight: 700,
      color: "#0f172a",
    },

    h5: {
      fontWeight: 700,
      color: "#0f172a",
    },

    h6: {
      fontWeight: 700,
      color: "#0f172a",
    },

    body1: {
      color: "#334155",
    },

    body2: {
      color: "#475569",
    },
  },
});

export default theme;