import Sidebar from "../components/Sidebar"
import { changeServer, server } from "../config"
import { useState } from "react"


function Server() {
    const [input, setInput] = useState('')
    const [serverInput, setServerInput] = useState('')

    function handleInputChange(event) {
        setInput(event.target.value)
        console.log(input)
        console.log({server})
    }

    changeServer(serverInput)

    return (
        <div>
            <Sidebar/>
            <input onChange={handleInputChange} className="border ml-64"></input>
            <p className="border bg-slate-400 ml-64">{server}</p>
            <button className="border bg-slate-400 ml-64" onClick={() => setServerInput(input)}>SAVE</button>
        </div>
    )
}

export default Server