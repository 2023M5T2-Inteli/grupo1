import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Sidebar from "../components/Sidebar"

const Profile = () => {
  const [clients, setClients] = useState([]);
  const [selectedClient, setSelectedClient] = useState('');
  const [newClientName, setNewClientName] = useState('');
  const [newClientCnpj, setNewClientCnpj] = useState('');
  const [newProjectName, setNewProjectName] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/client')
      .then(response => {
        setClients(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const handleNewClientSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:5000/client', {
      full_name: newClientName,
      cnpj: newClientCnpj
    })
      .then(response => {
        setClients([...clients, response.data]);
        setNewClientName('');
        setNewClientCnpj('');
      })
      .catch(error => {
        console.log(error);
      });
  };

  const handleNewProjectSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:5000/project', {
      client_id: selectedClient,
      full_name: newProjectName
    })
      .then(response => {
        console.log(response.data);
        setNewProjectName('');
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <div>
        <div>
            <Sidebar/>
            
        </div>
        
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center',  }} >
    
      <div  style={{ display: 'inline-block', marginTop: '20%', display: 'flex', justifyContent: 'center', alignItems: 'center' }} className="ml-20 flex flex-col items-center justify-center flex flex-wrap space-x-3">
      
        <h2>Cliente</h2>
        <form style={{ marginTop: '15px', display: 'flex', justifyContent: 'center', alignItems: 'center' }} className="pr-5 pl-2 flex flex-col justify-between"onSubmit={handleNewClientSubmit}>
          <label>
            Nome:
            <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="text" value={newClientName} onChange={(event) => setNewClientName(event.target.value)} />
          </label>
          <label>
            CNPJ:
            <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="text" value={newClientCnpj} onChange={(event) => setNewClientCnpj(event.target.value)} />
          </label>
          <button style={{ marginTop: '15px' }} className="font-montserrat font-bold text-white bg-indigo-900 w-4/12 h-9 rounded-xl shadow-xl  hover:scale-105 hover:bg-indigo-800  " type="submit">Enviar</button>
        </form>
      </div>
      <div style={{ display: 'inline-block', marginTop: '20%',display: 'flex', justifyContent: 'center', alignItems: 'center'  }} className="flex flex-wrap space-x-3 ml-20 flex flex-col">
        <h2>Projeto</h2>
        <form style={{ marginTop: '15px',  display: 'flex', justifyContent: 'center', alignItems: 'center' }} className="pr-5 pl-2 flex flex-col justify-between" onSubmit={handleNewProjectSubmit}>
          <label>
            Cliente:
            <select value={selectedClient} onChange={(event) => setSelectedClient(event.target.value)}>
              <option value="">Selecione um cliente</option>
              {clients.map(client => ( 
                <option  {...console.log(client)} key={client.id} value={client.id}>{client.full_name}</option>
              ))}
            </select>
          </label>
          
          <label>
            Nome:
            <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="text" value={newProjectName} onChange={(event) => setNewProjectName(event.target.value)} />
          </label>
          <button style={{ marginTop: '15px' }}className="font-montserrat font-bold text-white bg-indigo-900 w-4/12 h-9 rounded-xl shadow-xl  hover:scale-105 hover:bg-indigo-800  "  type="submit">Enviar</button>
        </form>
      </div>
    </div>
    </div>
  );
};

export default Profile;