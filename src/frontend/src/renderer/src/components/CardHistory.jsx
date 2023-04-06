import finalizado from '../assets/finalizado_icon.svg'
import { useState, useEffect } from 'react'
import jsPDF from 'jspdf'
import 'jspdf-autotable'


function Card(props) {

    const data_inicio = String(props.info.initiated_at).replace('Wed, ', '').replace(' GMT', '')
    const hora_inicio = String(props.info.initiated_at).slice(17, 25)
    const hora_fim = String(props.info.finished_at).slice(17, 25)
  
  //const hora = String(props.data).replace('Wed, ', '').replace(' GMT', '')

  const [showPopup, setShowPopup] = useState(false)

  const handleCardClick = () => {
    setShowPopup(true)
  }

  const handleCloseClick = () => {
    setShowPopup(false)
  }
  const [project, setProject] = useState('')
  const [client, setClient] = useState('')
  const [user, setUser] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:5000/project/' + props.info.project_id)
      .then((response) => response.json())
      .then((data) => {
        setProject(data)
        fetch('http://127.0.0.1:5000/client/' + project.client_id)
          .then((response) => response.json())
          .then((data) => setClient(data))
      })

      fetch('http://127.0.0.1:5000/user/' + props.info.user_id)
      .then((response) => response.json())
      .then((data) => {
        setUser(data)
      })
  }, [project])

  
  return (
    <>
      <div
        onClick={handleCardClick}
        className="shadow-2xl rounded-3xl md:w-1/4 flex flex-col justify-center items-center h-96 max-w-s mx-4 mb-8 hover:scale-105"
      >
        <img className="pb-10" src={finalizado} />
        <h3 className="font-montserrat font-bold p-3 text-2xl">Amostra #{props.id}</h3>
        <div className="flex flex-wrap space-x-3">
          <p className="font-montserrat font-medium">Data</p>
          <p className="font-montserrat object-right">{props.data}</p>
        </div>
        <div className="flex flex-wrap space-x-3">
          <p className="font-montserrat font-medium">Peso</p>
          <p className="font-montserrat object-right">{props.massa}</p>
        </div>
      </div>
      {showPopup && (
        
        // Add your popup component here
        <div className="fixed inset-0 flex justify-center items-center bg-gray-500 bg-opacity-50">
          <div className="bg-white w-3/4 h-3/4 rounded-lg">
            <div className="flex items-center justify-between p-5 border-b rounded-t dark:border-gray-600">
              <h1 className="text-4xl font-bold font-montserrat mb-4 pt-4 pl-4">
                Amostra: #{props.id}
              </h1>
              <button
                type="button"
                onClick={handleCloseClick}
                className="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
                data-modal-hide="extralarge-modal"
              >
                <svg
                  aria-hidden="true"
                  className="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fillRule="evenodd"
                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                    clipRule="evenodd"
                  ></path>
                </svg>
              </button>
            </div>
            <div className="pl-12 pr-12 pt-8 pb-8 flex items-center ">
              <div className="w-1/2">
                <h5 className="text-xl font-montserrat font-medium">
                  Nome da amostra: {props.name}
                </h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">Nome do cliente: {client.full_name}</h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">Data: {data_inicio}</h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">Horário de início: {hora_inicio}</h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">Horário de termino: {hora_fim}</h5>
                <br />
              </div>
              <div className="w-1/2">
                <h5 className="text-xl font-montserrat font-medium">Operador: {user.full_name}</h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">
                  Massa inicial dos sólidos: {props.mass}
                </h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">
                  Massa inicial da água: {props.water}
                </h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">
                  Campo magnético utilizado: {}
                </h5>
                <br />
                <h5 className="text-xl font-montserrat font-medium">Tempo do ciclo: {}</h5>
                <br />
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  )
}
export default Card
