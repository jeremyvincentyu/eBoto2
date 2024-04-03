import './App.css'
import {Outlet} from "react-router-dom";
import {Box} from "@mui/material"
function App() {

  return (
    <Box>
    <Outlet/>
    </Box>
  )
}

export default App
