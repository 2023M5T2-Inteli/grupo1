// Página para adicionar novos clientes, usuários e projetos

import Sidebar from "../components/Sidebar"
import { UserTable } from '../components/UserTable';
import { ClientTable } from '../components/ClientTable';

const Add = () => {

  return (
    <div className='h-screen'>
      <Sidebar />
      <div className="ml-20 flex items-center justify-center h-screen">
        <div className="flex justify-center gap-16">
          <ClientTable />
          <UserTable />
        </div>
      </div>
    </div>
  );
};

export default Add;