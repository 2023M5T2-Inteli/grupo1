// Página de início
import Sidebar from "../components/Sidebar"
import { Form } from "../components/Form";

function Home() {
  return (
    <div className="w-full h-screen">
      <Sidebar />
      {/* Div de conteúdo principal (ao lado da sidebar) */}
      <div className="ml-20 flex flex-col items-center justify-center">
        <Form/>         
      </div>
    </div>
  );
}

export default Home