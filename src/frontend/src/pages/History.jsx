import finalizado from '../assets/finalizado_icon.svg'
function History() {
return (
    <div className='mx-auto max-w-7xl mb-8'>
        <h1 className="font-montserrat font-bold text-4xl box-border p-16">Histórico de ensaios</h1>
        <div  className="flex justify-end mb-10">
            <select className="font-montserrat bg-gray-300 text-center	w-2/12 h-9 font-bold rounded-xl mr-4">
                <option className='bg-neutral-600'>Tipo de material</option>
                <option value="opcao1">Ferro</option>
                <option value="opcao2">Ouro</option>
                <option value="opcao3">Cobre</option>
                <option value="opcao3">Outros</option>
            </select>
            <input type="date" className="font-montserrat bg-gray-300 w-2/12 h-9 font-bold rounded-xl text-center mr-4"></input>
            <button className="font-montserrat font-bold text-white bg-indigo-900 w-1/12 h-9 rounded-xl shadow-xl">Filtrar</button>
        </div>
        <div className="w-ful flex flex-wrap">
            <div className="shadow-2xl rounded-3xl md:w-1/4 flex flex-col justify-center items-center h-96 max-w-s mx-8 mb-8"> 
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
            
            
            
        
        
        </div>
        
        
    </div>
    
);
}

export default History;