import './App.css'
import { useState, useEffect } from 'react'
import Axios from 'axios'

function App() {
  const [cycleCount, setCycleCount] = useState(0)
  const startTrial = () => {
    Axios.get('http://127.0.0.1:5000/start_trial')
      .then((res) => { console.log(res.data) })
  }
  const getCycleCount = () => {
    Axios.get('http://127.0.0.1:5000/cycleCount')
      .then((res) => { setCycleCount(res.data) })
  }
  useEffect(() => {
    const myInterval = setInterval(getCycleCount, 500);

    return () => {
      // should clear the interval when the component unmounts
      clearInterval(myInterval);
    };
  }, []);
  return (
    <div className="App">
      <button onClick={startTrial}>START TRIAL</button>
      <h1>Cycle count: {cycleCount}</h1>
    </div>
  )
}

export default App
