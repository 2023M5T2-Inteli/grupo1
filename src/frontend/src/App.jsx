/* Este é um app em React. A página principal se encontra neste script, utilizando componentes de 
outros scrips da pasta "components". 
*/

// Importa recursos necessários 
import { useState, useEffect } from 'react' // Hook para controlar estado dos componentes
import Axios from 'axios' // Biblioteca para fazer requisições HTTP
import bgWaves from './assets/bg-waves.png' // Vetor de decoração na base da página
import Button from './components/Button'

// Componente principal
function App() {
  // Declaração dos hooks de estado
  const [cycleCount, setCycleCount] = useState(0) // Contagem de ciclos atual
  const [magnetState, setMagnetState] = useState(0) // Estado do ímã
  const [pumpState, setPumpState] = useState(0) // Estado da bomba d'água
  const [sensorState, setSensorState] = useState(0) // Estado da sensor magnético

  // Declaração do endereço do servidor atual
  const serverHost = 'http://127.0.0.1:5000'

  // Função para trocar estado do ímã. Como ainda não fizemos rotas de POST, essa mudança
  // no servidor é feita através de diferentes rotas de GET
  const toggleMagnet = () => {
    if (magnetState) { // Se o valor atual é maior do que 0, uma requisição é feita para a rota que  desliga o ímã
      Axios.get(serverHost + '/disable_magnet') // requisição
        .then((res) => {
          setMagnetState(0) // troca estado no script para 0
        })
    } else { // se o valor é 0, liga ímã e troca estado
      Axios.get(serverHost + '/enable_magnet')
        .then((res) => {
          setMagnetState(1)
        })
    }
  }

  // Função para trocar estado da bomba. Segue a mesma lógica do ímã.
  const togglePump = () => {
    if (pumpState) {
      Axios.get(serverHost + '/disable_pump')
        .then((res) => {
          setPumpState(0)
        })
    } else {
      Axios.get(serverHost + '/enable_pump')
        .then((res) => {
          setPumpState(1)
        })
    }
  }

  // Função para trocar estado da bomba. Segue a mesma lógica dos dois anteriores.
  const toggleSensor = () => {
    if (sensorState) {
      Axios.get(serverHost + '/disable_sensor')
        .then((res) => {
          setSensorState(0)
        })
    } else {
      Axios.get(serverHost + '/enable_sensor')
        .then((res) => {
          setSensorState(1)
        })
    }
  }

  // Função que faz requisição ao servidor para começar o ensaio com o robô
  const startTrial = () => {
    Axios.get(serverHost + '/start_trial')
      .then((res) => { })
  }

  // Função que faz requisição ao servidor para ler o número de ciclos atual
  const getCycleCount = () => {
    Axios.get(serverHost + '/cycleCount')
      .then((res) => { setCycleCount(res.data) }) // Atualiza estado com o valor lido
  }

  // Função que faz requisição ao servidor para ler o estado do ímã e da bomba atualmente.
  // O objetivo é eventualmente utilizar essa função para receber erros do servidor.
  const getStates = () => {
    Axios.get(serverHost + '/states')
      .then((res) => {
        // Atualiza estados no frontend
        setMagnetState(Number.parseInt(res.data.magnet))
        setPumpState(Number.parseInt(res.data.pump))
        setPumpState(Number.parseInt(res.data.sensor))
      })
  }

  // Executa funções para atualizar estados
  const updateData = () => {
    getCycleCount()
    getStates()
  }

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
      <Button onClick={toggleMagnet} content={magnetState ? "Desligar imã" : "Ligar imã"} />
      <Button onClick={togglePump} content={pumpState ? "Desligar bomba" : "Ligar bomba"} />
      <Button onClick={toggleSensor} content={sensorState ? "Desligar sensor" : "Ligar sensor"} />
      <h1>Cycle count: {cycleCount}</h1>
      <img className='fixed bottom-0' src={bgWaves} />
    </div>
  )
}

export default App
