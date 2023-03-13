// Página de demonstração para testes

import { useState, useEffect } from "react"; 
import { useNavigate } from "react-router-dom"; // Biblioteca para navegação entre páginas
import backDemo from '../assets/backDemo.png' // Botão de voltar

import Axios from "axios"; // Biblioteca para fazer requisições HTTP
import bgWaves from "../assets/bg-waves.png"; // Vetor de decoração na base da página

import Button from "../components/Button";

function Demo() {

    // Declaração dos hooks
    const [cycleCount, setCycleCount] = useState(0); 
    const [magnetState, setMagnetState] = useState(false); 
    const [pumpState, setPumpState] = useState(0);
    const navigate = useNavigate()
    

    // Declaração do endereço do servidor atual
    const serverHost = "http://10.128.20.240:5000";

    // Faz requisição ao servidor para trocar estado e atualiza estado local
    const toggleMagnet = () => {
        fetch(serverHost + "/toggle_magnet", {
            method: "POST",
            body: JSON.stringify({
                magnet_state: !magnetState
            }),
            headers: { "Content-type": "application/json;charset=UTF-8" },
        })
            .then((response) => response.json())
            .then((data) => console.log(data));

        setMagnetState(!magnetState)
    };

    // Faz requisição ao servidor para trocar estado e atualiza estado local
    const togglePump = () => {
        fetch(serverHost + "/toggle_pump", {
            method: "POST",
            body: JSON.stringify({
                pump_state: !pumpState
            }),
            headers: { "Content-type": "application/json;charset=UTF-8" },
        })
            .then((response) => response.json())
            .then((data) => console.log(data));

        setPumpState(!pumpState)
    };

    // Faz requisição ao servidor para iniciar ensaio
    const startTrial = () => {
        fetch(serverHost + "/start_trial").then((res) => { });
    };

    // Faz requisição ao servidor para ler valor e atualiza estado local
    const getCycleCount = () => {
        Axios.get(serverHost + "/cycleCount").then((res) => {
            setCycleCount(res.data);
        }); // Atualiza estado com o valor lido
    };

    // Faz requisição ao servidor para ler estados dos componentes e atualiza estados locais
    const getStates = () => {
        fetch(serverHost + '/states')
            .then(res => res.json())
            .then(data => {
                setMagnetState(Number.parseInt(data.magnet))
                setPumpState(Number.parseInt(data.pump))
            })
    }

    // Executa funções para atualizar estados
    const updateData = () => {
        getCycleCount();
        getStates();
    };

    // Hook para atualizar dados regularmente (a cada 1 segundo)
    useEffect(() => {
        const myInterval = setInterval(updateData, 1000); // Cria intervalo e chama função desejada
        return () => {
            clearInterval(myInterval); // Reinicia o intervalo
        };
    }, []);

    return (
        <div className="bg-background h-screen w-screen flex flex-col justify-center items-center">
            <button className="fixed left-3 top-3" onClick={() => navigate('/')}>
                <img src={backDemo} className="w-7"></img>
            </button>
            <Button onClick={startTrial} content="Iniciar ensaio" />
            <Button
                onClick={toggleMagnet}
                content={magnetState ? "Desligar imã" : "Ligar imã"}
            />
            <Button
                onClick={togglePump}
                content={pumpState ? "Desligar bomba" : "Ligar bomba"}
            />
            <h1>Cycle count: {cycleCount}</h1>
            <img className="fixed bottom-0 w-screen" src={bgWaves} />
        </div>
    );
}

export default Demo;