// Página de início

import { useRef, useState, useEffect } from "react";
import { useForm, FormProvider } from "react-hook-form";

import Sidebar from "../components/Sidebar"
import startButton from '../assets/startButton.png'
import Input from "../components/Input";

import RangeSlider from 'react-range-slider-input';
import 'react-range-slider-input/dist/style.css';

//Importando imagens 
import pumpIcon from '../assets/pumpIcon.png'
import turnOnIcon from '../assets/turnOnIcon.png'
import magnetIcon from '../assets/sidebarMagnet.png'
import seeMore from '../assets/seeMoreArrow.png'

import Axios from 'axios'

const Trays = {
  0: "DESATIVADO",
  1: "CAPTURA",
  2: "LIMPEZA",
  3: "DESPEJO",
}

function Home() {
  // Definição de hooks
  const [intensity, setIntensity] = useState([0, 12])
  const [cycleCount, setCycleCount] = useState(0);
  const [magnetState, setMagnetState] = useState(false);
  const [pumpState, setPumpState] = useState(0);
  const [currentTray, setCurrentTray] = useState(Trays[0]);

  const detailsRef = useRef();

  const methods = useForm();
  const watchAmostra = methods.watch("amostra")

  // Declaração do endereço do servidor atual
  const serverHost = "http://10.128.0.159:5000";

  // Desliza tela para card de detalhes
  function showDetails() {
    detailsRef.current.scrollIntoView({ behavior: 'smooth' });
  }

  // Faz requisição ao servidor para trocar estado e atualiza estado local
  const toggleMagnet = () => {
    fetch(serverHost + "/toggle_magnet", {
      method: "POST",
      body: JSON.stringify({
        magnet_state: !magnetState,
      }),
      headers: { "Content-type": "application/json;charset=UTF-8" },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));

    setMagnetState(!magnetState);
  };

  // Faz requisição ao servidor para trocar estado e atualiza estado local
  const togglePump = () => {
    fetch(serverHost + "/toggle_pump", {
      method: "POST",
      body: JSON.stringify({
        pump_state: !pumpState,
      }),
      headers: { "Content-type": "application/json;charset=UTF-8" },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));

    setPumpState(!pumpState);
  };

  // Faz requisição ao servidor para ler valor e atualiza estado local
  const getCycleCount = () => {
    Axios.get(serverHost + "/cycleCount").then((res) => {
      setCycleCount(res.data.cycleCount);
    }); // Atualiza estado com o valor lido
  };


  const getStates = () => {
    fetch(serverHost + "/states")
      .then((res) => res.json())
      .then((data) => {
        setMagnetState(Number.parseInt(data.magnet));
        setPumpState(Number.parseInt(data.pump));
      });
  };

  const getCurrentTray = () => {
    fetch(serverHost + "/current_tray")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTray(Trays[Number.parseInt(data.current_tray)]);
        console.log(data.current_tray)
      });
  };

  // Executa funções para atualizar estados
  const updateData = () => {
    getCycleCount();
    getStates();
    getCurrentTray();
    changeIntensity();
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
  function handleCreateNewCycle(data) {
    Axios.get(serverHost + "/start_trial").then((res) => {
      setCycleCount(res.data.cycleCount);
    }); // Atualiza estado com o valor lido
  }

  function changeIntensity() {
    fetch(serverHost + "/change_magnet_intensity", {
      method: "POST",
      body: JSON.stringify({
        magnet_intensity: intensity[1],
      }),
      headers: { "Content-type": "application/json;charset=UTF-8" },
    })
      .then((response) => response.json())
      .then((data) => console.log(data));

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
              <button type="submit" disabled={!watchAmostra} className={allowPointer()}>
                <img className={allowButton()} src={startButton} />
              </button>
              <div>
                <h1 className="text-3xl font-bold mb-5 font-montserrat">
                  Novo ensaio
                </h1>
                <div className="flex">
                  {/* Grupo de inputs de informações */}
                  <div className="pr-5 pl-2 flex flex-col justify-between">
                    <p className="text-slate-500 small-caps font-montserrat">
                      INFORMAÇÕES
                    </p>
                    <Input title="amostra" type="text" />
                    <Input title="cliente" type="text" />
                    <Input title="peso" type="number" />
                    <Input title="data" type="date" />
                    <Input title="horário" type="time" />
                    <Input title="duração" type="text" />
                  </div>

                  {/* Grupo de controles */}
                  <div className="pr-5 pl-2 w-96 flex flex-col justify-between gap-4">
                    <p className="text-slate-500 small-caps font-montserrat">
                      CONTROLES
                    </p>

                    <span className="flex gap-5 justify-around">
                      {/* <button>
                        <img
                          className="w-9 hover:scale-105"
                          src={turnOnIcon}
                          onClick={}
                        ></img>
                      </button> */}
                      <button>
                        <img
                          className="w-9 hover:scale-105"
                          src={magnetIcon}
                          onClick={toggleMagnet}
                        ></img>
                      </button>
                      <button>
                        <img
                          className="w-9 hover:scale-105"
                          src={pumpIcon}
                          onClick={togglePump}
                        ></img>
                      </button>
                    </span>

                    <p className="font-bold font-montserrat">
                      Intensidade do ímã:{" "}
                    </p>

                    <span
                      id="sliderWrapper"
                      className="flex gap-2 items-center justify-center font-montserrat"
                    >
                      {/* Slider */}
                      <RangeSlider
                        min={0}
                        max={12}
                        thumbsDisabled={[true, false]}
                        value={intensity}
                        onInput={setIntensity}
                      />
                      <p>{intensity[1] + "V"}</p>
                    </span>

                    <span className="flex gap-2">
                      <p className="font-bold font-montserrat">Ciclo: </p>
                      <p className="font-montserrat">{cycleCount}</p>
                    </span>

                    <span className="flex gap-2 font-montserrat">
                      <p className="font-bold">Status: </p>
                      <p>{currentTray}</p>
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </FormProvider>
        {/* Botão para mostrar card de mais detalhes */}
        <button
          className="w-14 absolute bottom-5 flex justify-center"
          onClick={showDetails}
        >
          <img src={seeMore} />
        </button>
        {/* Card de mais informações */}
        <div
          className="w-[90%] h-96 bg-white rounded-xl shadow-2xl m-5 flex justify-center items-center"
          ref={detailsRef}
        >
          MAIS INFORMAÇÕES
        </div>
      </div>
    </div>
  );
}

export default Home