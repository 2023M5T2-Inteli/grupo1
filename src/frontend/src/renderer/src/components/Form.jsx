// Componente de formulário da página principal

import { useState, useEffect } from "react";
import { useForm, FormProvider } from "react-hook-form";
import startButton from '../assets/startButton.png'
import Axios from 'axios'
import { ActuatorControls } from "./ActuatorControls";

export function Form() {

  const methods = useForm(); // Inicializa o formulário

  // Declaração de estados
  const [sample, setSample] = useState("");
  const [initialSampleMass, setInitialSampleMass] = useState("");
  const [initialWaterMass, setInitialWaterMass] = useState("");
  const [clients, setClients] = useState([]);
  const [users, setUsers] = useState([]);
  const [projects, setProjects] = useState([]);
  const [selectedClient, setSelectedClient] = useState("");
  const [selectedProject, setSelectedProject] = useState("");
  const [selectedUser, setSelectedUser] = useState("");
  const [cycleNumber, setCycleNumber] = useState(0);
  const [routineId, setRoutineId] = useState(0);

  // Declaração do endereço do servidor atual
  const serverHost = "http://127.0.0.1:5000";

  // Hook para atualizar dados regularmente (a cada 1 segundo)
  useEffect(() => {
    fetchDropdowns()
  }, [])

  // Função que envia dados para o servidor
  function handleCreateNewCycle() {
    fetch(serverHost + "/routine", {

      method: "POST",
      body: JSON.stringify({
        client_id: selectedClient,
        sample_name: sample,
        initial_sample_mass: initialSampleMass,
        initial_water_mass: initialWaterMass,
        user_id: selectedUser,
        project_id: selectedProject,
        cycleCount: cycleNumber
      }),
      headers: { "Content-type": "application/json" }})
      then(response => response.json())
      .then(data => {
        setRoutineId(data.routine_id)
      })
  }

  // Função que rece dados do servidor para os dropdowns
  const fetchDropdowns = async () => {
    const clients = await Axios.get(serverHost + '/client');
    const users = await Axios.get(serverHost + '/user');
    const projects = await Axios.get(serverHost + '/project');
    setClients(clients.data);
    setUsers(users.data);
    setProjects(projects.data);
  }

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(handleCreateNewCycle)}>
        <div className="flex h-screen items-center gap-10 justify-center">
          {/* Botão de iniciar ensaio */}
          <button type="submit"   >
            <img src={startButton} />
          </button>
          <div>
            <h1 className="text-3xl font-bold mb-5 font-montserrat">
              Novo Ensaio
            </h1>
            <div className="flex">
              {/* Grupo de inputs de informações */}
              <div className="pr-5 pl-2 flex flex-col justify-between">
                <p className="text-slate-500 small-caps font-montserrat">
                  INFORMAÇÕES
                </p>
                <label>
                  Amostra:
                  <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="text" value={sample} onChange={(event) => setSample(event.target.value)} />
                </label>
                <br />
                <label htmlFor="clients">Cliente:</label>
                <select id="clients" value={selectedClient} onChange={(e) => setSelectedClient(e.target.value)}>
                  <option value="">Selecione um cliente</option>
                  {clients.map(client => (
                    <option key={client.id} value={client.id}>{client.full_name}</option>
                  ))}
                </select>
                <br />
                <label htmlFor="projects">Projeto:</label>
                <select id="projects" value={selectedProject} onChange={(e) => setSelectedProject(e.target.value)}>
                  <option value="">Selecione um projeto</option>
                  {
                    projects.filter(project => project.client_id == selectedClient).map(project => (
                      <option key={project.id} value={project.id}>{project.name}</option>
                    ))}
                </select>
                <br />
                <label htmlFor="users">Operador:</label>
                <select id="users" value={selectedUser} onChange={(e) => setSelectedUser(e.target.value)}>
                  <option value="">Selecione um operador</option>
                  {
                    users.map(user => (
                      <option key={user.id} value={user.id}>{user.full_name}</option>
                    ))}
                </select>
                <br />
                <label>
                  Massa do sólido:
                  <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="number" value={initialSampleMass} onChange={(event) => setInitialSampleMass(event.target.value)} />
                </label>
                <br />
                <label>
                  Massa da água:
                  <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="number" value={initialWaterMass} onChange={(event) => setInitialWaterMass(event.target.value)} />
                </label>
                <br />
                <label>
                  Nº de ciclos:
                  <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" type="number" value={cycleNumber} onChange={(event) => setCycleNumber(event.target.value)} />
                </label>
              </div>
              {/* Grupo de inputs de atuadores */}
              <ActuatorControls />
            </div>
          </div>
        </div>
      </form>
    </FormProvider>
  )
}