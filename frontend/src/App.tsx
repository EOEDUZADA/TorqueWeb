
import { LoginForm } from "./components/login-form";
import Login from "./components/pages/Login";
import Clients from "@/components/pages/Clients";


function App() {
  return (
    <div className="flex min-h-svh w-full items-center justify-center p-6 md:p-10">
      <div className="w-full">
        <Clients />
      </div>
    </div>
  )
}

export default App;