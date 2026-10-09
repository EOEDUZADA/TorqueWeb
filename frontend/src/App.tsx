
import { BrowserRouter, Routes, Route, useParams } from "react-router";
import Login from "./components/pages/Login";
import Home from "./components/pages/Home";
import Clients from "./components/pages/Clients";
import Parts from "./components/pages/Parts";

function WorkOrderDetails() {
  const { id } = useParams();

  return <div>Detalhes da ordem de serviço: {id}</div>;
}

function NotFound() {
  return <div>Página não encontrada.</div>;
}

function App() {
  return (

  <div className=" p-6">
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Home />} />
        <Route path="/clientes" element={<Clients />} />
        <Route path="/pecas" element={<Parts />} />
        <Route path="/ordens/:id" element={<WorkOrderDetails />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  </div>
  );
}

export default App;