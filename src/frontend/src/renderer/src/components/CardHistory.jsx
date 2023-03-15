import finalizado from '../assets/finalizado_icon.svg'


function Card() {
    return (
        <div className="shadow-2xl rounded-3xl md:w-1/4 flex flex-col justify-center items-center h-96 max-w-s mx-4 mb-8 hover:scale-105"> 
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
    )
}

export default Card