// Página de início

import { useState, useEffect } from "react";
import { useForm, FormProvider } from "react-hook-form";

import Sidebar from "../components/Sidebar"
import startButton from '../assets/startButton.png'

import RangeSlider from "../components/Slider";

//Importando imagens 
import pumpIcon from '../assets/pumpIcon.png'
import magnetIcon from '../assets/sidebarMagnet.png'

import Axios from 'axios'

// "Enum" para estado das bandejas
const Trays = {
  0: "DESATIVADO",
  1: "CAPTURA",
  2: "LIMPEZA",
  3: "DESPEJO",
}

function Home() {
  // Definição de hooks
  const [intensity, setIntensity] = useState(0)
  const [cycleCount, setCycleCount] = useState(0);
  const [magnetState, setMagnetState] = useState(false);
  const [pumpState, setPumpState] = useState(0);
  const [currentTray, setCurrentTray] = useState(Trays[0]);
  let routine = 0

  const methods = useForm();
  const watchAmostra = methods.watch("amostra")

  // Declaração do endereço do servidor atual
  const serverHost = "http://127.0.0.1:5000";

  // Faz requisição ao servidor para trocar estado e atualiza estado local
  const toggleMagnet = () => {
    fetch(serverHost + "/current/magnet", {
      method: "POST",
      body: JSON.stringify({
        magnet_state: !Boolean(magnetState),
        magnet_intensity: intensity
      }),
      headers: { "Content-type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));

    setMagnetState(!magnetState);
  };

  // Faz requisição ao servidor para trocar estado e atualiza estado local
  const togglePump = () => {
    fetch(serverHost + "/current/pump", {
      method: "POST",
      body: JSON.stringify({
        pump_state: !pumpState,
      }),
      headers: { "Content-type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));

    setPumpState(!pumpState);
  };

  // Faz requisição ao servidor para ler valor e atualiza estado local
  const getCycleCount = () => {
    Axios.get(serverHost + "/current/cycle").then((res) => {
      setCycleCount(res.data.cycleCount);
    }); // Atualiza estado com o valor lido
  };

  // Faz requisição para estados atuais do ímã e da bomba
  const getStates = () => {
    fetch(serverHost + "/current/magnet")
      .then((res) => res.json())
      .then((data) => {
        setMagnetState(data.magnet_state);
      });
    fetch(serverHost + "/current/pump")
      .then((res) => res.json())
      .then((data) => {
        setPumpState(data.pump_state);
      });
  };

  // Devolve o estado atual da bandeja
  const getCurrentTray = () => {
    fetch(serverHost + "/current/tray")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTray(Trays[Number.parseInt(data['current_tray'])]);
      });
  };

  // Executa funções para atualizar estados
  const updateData = () => {
    getCycleCount();
    getStates();
    getCurrentTray();
    fetchCycles();
  };

  // Hook para atualizar dados regularmente (a cada 1 segundo)
  useEffect(() => {
    const myInterval = setInterval(updateData, 1000); // Cria intervalo e chama função desejada
    return () => {
      clearInterval(myInterval); // Reinicia o intervalo
    };
  }, []);

  //Função que muda o mouse ao passar pelo botão iniciar quando item amostra está preenchido
  function allowPointer() {
    if (watchAmostra) {
      return "cursor-pointer"
    }
    else {
      return "cursor-not-allowed"
    }
  }

  //Função que coloca efeito visual quando item amostra está preenchido
  function allowButton() {
    if (watchAmostra) {
      return "hover:scale-105"
    }
    else {
      return ""
    }
  }

  // Função que envia dados para o servidor (No momento so printa)
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
      headers: { "Content-type": "application/json" },
    }).then(response => response.json())
      .then(data => {
        setRoutineId(data.routine_id)
        console.log(routineId)
      })
  }

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
  const [cycles, setCycles] = useState([]);

  useEffect(() => {
    fetchDropdowns()
  }, [])

  const fetchDropdowns = async () => {
    const clients = await Axios.get(serverHost + '/client');
    const users = await Axios.get(serverHost + '/user');
    const projects = await Axios.get(serverHost + '/project');
    setClients(clients.data);
    setUsers(users.data);
    setProjects(projects.data);
  }

  const fetchCycles = async () => {
    console.log(routine)
    if (routine) {
      console.log('inside')
      fetch(serverHost + '/routine/' + routine).then((res) => res.json()).then((data) => {
        setCycles(data['cycles'])
        console.log({ cycles })
      })
    }
  }

  return (
    <div className="w-full h-screen">
      <Sidebar />
      {/* Div de conteúdo principal (ao lado da sidebar) */}
      <div className="ml-20 flex flex-col items-center justify-center">
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
                  {/* Grupo de controles */}
                  <div className="pr-5 pl-2 w-96 flex flex-col justify-between gap-4">
                    <p className="text-slate-500 small-caps font-montserrat">
                      CONTROLES
                    </p>

                    <span className="flex gap-5 justify-around">
                      <button type='button'>
                        <img
                          className="w-9 hover:scale-105"
                          src={magnetIcon}
                          onClick={toggleMagnet}
                        ></img>
                      </button>
                      <button type='button'>
                        <img
                          className="w-9 hover:scale-105"
                          src={pumpIcon}
                          onClick={togglePump}
                        ></img>
                      </button>
                    </span>

                    <span
                      className="flex gap-2 items-center justify-between font-montserrat w-full "
                    >
                      <p className="font-bold font-montserrat">
                        Intensidade do ímã:
                      </p>
                      <RangeSlider value={intensity} setValue={setIntensity} state={magnetState} />

                    </span>

                    <span className="flex gap-2 items-baseline">
                      <p className="font-bold font-montserrat">Ciclo: </p>
                      <p className="font-montserrat">{cycleCount}</p>
                    </span>

                    <span className="flex gap-2 font-montserrat items-baseline">
                      <p className="font-bold">Status: </p>
                      <p>{currentTray}</p>
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </FormProvider>
      </div>
    </div>
  );
}

export default Home