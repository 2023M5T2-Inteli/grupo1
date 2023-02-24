import { useState, useEffect } from 'react'
import Axios from 'axios'

function App() {
  const [cycleCount, setCycleCount] = useState(0)
  const [imaState, setImaState] = useState(0)

  const toggleIma = () => {
    if (imaState) {
      Axios.get('http://127.0.0.1:5000/desligar_ima')
        .then((res) => { 
          console.log(res.data)
          setImaState(0) 
      })
    } else {
      Axios.get('http://127.0.0.1:5000/ligar_ima')
        .then((res) => { 
          console.log(res.data)
          setImaState(1) 
      })
    }
  }

const startTrial = () => {
  Axios.get('http://127.0.0.1:5000/start_trial')
    .then((res) => { console.log(res.data) })
}

const getCycleCount = () => {
  Axios.get('http://127.0.0.1:5000/cycleCount')
    .then((res) => { setCycleCount(res.data) })
}

const getImaState = () => {
  Axios.get('http://127.0.0.1:5000/ima')
        .then((res) => { 
          console.log(res.data)
          setImaState(Number.parseInt(res.data)) 
      })
}

const updateData = () => {
  getCycleCount()
  getImaState()
}

useEffect(() => {
  const myInterval = setInterval(updateData, 1000);

  return () => {
    // should clear the interval when the component unmounts
    clearInterval(myInterval);
  };
}, []);
return (
  <div className="bg-background h-screen w-screen flex flex-row justify-center items-center">
    <button className="text-green" onClick={startTrial}>START TRIAL</button>
    <button onClick={toggleIma}>{imaState ? "Desligar imã" : "Iniciar imã"}</button>
    <h1>Cycle count: {cycleCount}</h1>
  </div>
)
}

export default App
