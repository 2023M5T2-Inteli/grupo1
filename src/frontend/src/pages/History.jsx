import finalizado from '../assets/finalizado_icon.svg'
function History() {
return (
    <div className='mx-auto max-w-7xl mb-8'>
        <h1 className="font-montserrat font-bold text-4xl box-border p-16">Histórico de ensaios</h1>
        <div  className="flex justify-end">
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

        <divcd > 
            <img className="" src={finalizado} />
            <h3>Amostra #1233</h3>
            <p>Data 00/00/0000</p>
            <p>Peso 500gm</p>

        </divcd>
        
    </div>
    
);
}

export default History;