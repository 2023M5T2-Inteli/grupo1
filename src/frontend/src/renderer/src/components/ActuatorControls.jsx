// Componente de controle dos atuadores

// Slider de intensidade
import RangeSlider from "../components/Slider";

import { useState, useEffect } from "react";
import Axios from 'axios'

// Importando imagens 
import pumpIcon from '../assets/pumpIcon.png'
import magnetIcon from '../assets/sidebarMagnet.png'

// "Enum" para estado das bandejas
const Trays = {
    0: "DESATIVADO",
    1: "CAPTURA",
    2: "LIMPEZA",
    3: "DESPEJO",
}

export function ActuatorControls() {

    // Define estados
    const [intensity, setIntensity] = useState(0)
    const [cycleCount, setCycleCount] = useState(0);
    const [magnetState, setMagnetState] = useState(false);
    const [pumpState, setPumpState] = useState(0);
    const [currentTray, setCurrentTray] = useState(Trays[0]);


    let routine = 0

    // Declaração do endereço do servidor atual
    const serverHost = "http://127.0.0.1:5000";

    // Hook para atualizar dados regularmente (a cada 1 segundo)
    useEffect(() => {
        const myInterval = setInterval(updateData, 1000); // Cria intervalo e chama função desejada
        return () => {
            clearInterval(myInterval); // Reinicia o intervalo
        };
    }, []);

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
        });
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

    // Lê ciclos de certa rotina
    const fetchCycles = async () => {
        if (routine) {
            fetch(serverHost + '/routine/' + routine).then((res) => res.json()).then((data) => {
                setCycles(data['cycles'])
            })
        }
    }
    
    return (
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
    )
}