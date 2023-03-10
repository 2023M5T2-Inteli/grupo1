/* Este é um app em React. A página principal se encontra neste script, utilizando componentes de 
outros scrips da pasta "components". 
*/

// Importa recursos necessários
import { useState, useEffect } from "react"; // Hook para controlar estado dos componentes
import Axios from "axios"; // Biblioteca para fazer requisições HTTP
import bgWaves from "./assets/bg-waves.png"; // Vetor de decoração na base da página
import Button from "./components/Button";

// Componente principal
function App() {
  // Declaração dos hooks de estado
  const [cycleCount, setCycleCount] = useState(0); // Contagem de ciclos atual
  const [magnetState, setMagnetState] = useState(false); // Estado do ímã
  const [pumpState, setPumpState] = useState(0); // Estado da bomba d'água

  // Declaração do endereço do servidor atual
  const serverHost = "http://10.128.64.149:5000";


  // Função para trocar estado do ímã. Como ainda não fizemos rotas de POST, essa mudança
  // no servidor é feita através de diferentes rotas de GET
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

  // Função para trocar estado da bomba. Segue a mesma lógica do ímã.
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

  // Função que faz requisição ao servidor para começar o ensaio com o robô
  const startTrial = () => {
    fetch(serverHost + "/start_trial").then((res) => {});
  };

  // Função que faz requisição ao servidor para ler o número de ciclos atual
  const getCycleCount = () => {
    Axios.get(serverHost + "/cycleCount").then((res) => {
      setCycleCount(res.data);
    }); // Atualiza estado com o valor lido
  };

  // Função que faz requisição ao servidor para ler o estado do ímã e da bomba atualmente.
  // O objetivo é eventualmente utilizar essa função para receber erros do servidor.
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

  // Hook atualizar dados regularmente (a cada 1 segundo)
  useEffect(() => {
    const myInterval = setInterval(updateData, 1000); // Cria intervalo e chama função desejada
    return () => {
      clearInterval(myInterval); // Reinicia o intervalo
    };
  }, []);

  // Elementos a serem mostrados na tela
  return (
    <div className="bg-background h-screen w-screen flex flex-col justify-center items-center">
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
      <img className="fixed bottom-0" src={bgWaves} />
    </div>
  );
}

export default App;
