import finalizado from '../assets/finalizado_icon.svg'
import { useState } from 'react'

function Card() {
    const [showPopup, setShowPopup] = useState(false)

    const handleCardClick = () => {
        setShowPopup(true)
    }

    const handleCloseClick = () => {
        setShowPopup(false)
    }

    return (
        <>
            <div onClick={handleCardClick} className="shadow-2xl rounded-3xl md:w-1/4 flex flex-col justify-center items-center h-96 max-w-s mx-4 mb-8 hover:scale-105"> 
                <img className="pb-10" src={finalizado} />
                <h3 className="font-montserrat font-bold p-3 text-2xl">Amostra #1233</h3>
                <div className="flex flex-wrap space-x-3">
                    <p className="font-montserrat font-medium">Data</p>
                    <p className="font-montserrat object-right">00/00/0000</p>
                </div>
                <div className="flex flex-wrap space-x-3">
                    <p className="font-montserrat font-medium">Peso</p>
                    <p className="font-montserrat object-right">550mg</p>
                </div>    
            </div>

            {showPopup && (
                // Add your popup component here
                <>
                    <div style={{position: 'fixed', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', backgroundColor: 'white', padding: '20px', borderRadius: '10px', zIndex: 9999}}>
                        <button onClick={handleCloseClick} style={{position: 'absolute', top: 0, right: 0}}>X</button>
                        {/* Divide information into two columns */}
                        <strong><h2 style={{textAlign:'center'}}>Amostra:XXXX</h2></strong>
                        {/* Align columns to the top */}
                        <div style={{display:'flex', alignItems:'flex-start'}}>
                            {/* First column */}
                            
                            <div style={{flex:'1'}}>
                            <strong><h2>Uma unica vez:</h2></strong>
                                Data:XXXX<br />
                                Horário:XXXX<br />
                                Nome da amostra:XXXX<br />
                                Nome do cliente:XXXX<br />
                                Nome do projeto:XXXX<br />
                                Usuario/operador:XXXX<br />
                                Massa incial solidos:XXXX<br />
                                Massa incial de agua:XXXX<br />
                                Duração:XXXX<br />
                            </div>
                            
                            {/* Second column */}
                            <div style={{flex:'1'}}>
                            <strong><h2>Uma vez por ciclo:</h2></strong>
                                Numero do ciclo:XXXX<br />
                                Camp magnético utlizado:XXXX<br />
                                Masso por ciclo (se possivel): XXXX<br />
                                Tempo por ciclo (se possivel): XXXX<br />
                           </div>
                       </div>

                   </div>
               </>
           )}
       </>
   )
}

export default Card;