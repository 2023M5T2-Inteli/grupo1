// Importa recursos necessários 
import Axios from 'axios' // Biblioteca para fazer requisições HTTP
import Sidebar from '../components/Sidebar'
import startButton from '../assets/startButton.png'

// Componente principal
function Ancient() {

  // Declaração do endereço do servidor atual
  const serverHost = 'http://10.128.20.240:5000'

  // Elementos a serem mostrados na tela
  return (
  <div className="grid grid-cols-12 gap-7 h-full">
    <div className="col-span-2"><Sidebar/></div>
    <div className="flex transform transition duration-300 shadow-2xl rounded-lg col-span-9 bg-white mt-3 p-5">
      <div className="justify-between">
        <button><img className="hover:scale-105 p-2 w-[300px]" src={startButton}></img></button>
      </div>
      <div className='ml-7 flex-1'>
        <div className="mt-3 text-3xl font-bold leading-8 font-family-Montserrat">Amostra #0000</div>
        <div className='mt-10'>
          <div>
            <a className='mt-8 font-family-Montserrat text-xl font-semibold text-left'>Data:</a>
          </div>
          <div>
            <div className='mt-8 font-family-Montserrat text-xl font-semibold'>Peso:</div>
          </div>
          <div>
            <div className='mt-8 font-family-Montserrat text-xl font-semibold'>Horário de Início:</div>
          </div>
        </div>
        <div className="absolute mr-10 mb-3 text-xl font-bold text-gray-600 left-30px text-right right-0 bottom-0">Duração</div>
      </div>
    </div>

    <div className='col-start-3 col-end-5'>
      <div className="mt-3 text-3xl font-bold leading-8 font-family-Montserrat flex ">Último Ensaio:</div>
    </div>

    <div className="flex transform transition duration-300 shadow-2xl rounded-lg col-start-3 col-end-12 bg-white mt-3 p-5">
      <div className="justify-between">
        <button><img className="hover:scale-105 p-2 w-[150px]" src={startButton}></img></button>
      </div>
      <div className='ml-7 flex-1'>
        <div className="mt-3 text-3xl font-bold leading-8 font-family-Montserrat">Novo ensaio</div>
        <div>
            <div>
              <div className='mt-4 font-family-Montserrat text-xl font-semibold text-left'>Data:</div>
            </div>
            <div>
              <div className='mt-4 font-family-Montserrat text-xl font-semibold text-left'>Peso:</div>
            </div> 
        </div>
        <div className="absolute mr-10 mb-3 text-xl font-bold text-gray-600 left-30px text-right right-0 bottom-0">Duração</div>
      </div>
    </div>

  </div>
  )
}

export default Ancient

