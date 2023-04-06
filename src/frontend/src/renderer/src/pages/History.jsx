// Script para a página de histórico de ensaios
import { useEffect, useState } from 'react';
import Card from '../components/CardHistory'
import Sidebar from '../components/Sidebar';
function History() {
    // Faz requisição para pegar as informações do histórico
    const [cards, all_cards] = useState([]);
    const get_all_cards = async (url) =>{
        const res = await fetch(url);
        const data = await res.json();
        console.log(data)
        all_cards(data);
    };
    useEffect(() =>{
            let url = "http://127.0.0.1:5000"
            get_all_cards(url+"/routine")
        },[]);
    return (
        <div>
            <Sidebar />
            <div className='ml-20 max-w-7xl mb-8'>
                <h1 className="font-montserrat font-bold text-4xl box-border p-16">Histórico de ensaios</h1>
                <div className="flex justify-end mb-10">
                    <select className="font-montserrat bg-gray-300 text-center  w-2/12 h-9 font-bold rounded-xl mr-4 cursor-pointer hover:scale-105">
                        <option className='bg-neutral-600' disabled>Tipo de material</option>
                        <option value="opcao1">Ferro</option>
                        <option value="opcao2">Ouro</option>
                        <option value="opcao3">Cobre</option>
                        <option value="opcao3">Outros</option>
                    </select>
                    <input type="date" className="font-montserrat bg-gray-300 w-2/12 h-9 font-bold rounded-xl text-center mr-4 cursor-pointer hover:scale-105"></input>
                    <button className="font-montserrat font-bold text-white bg-indigo-900 w-1/12 h-9 rounded-xl shadow-xl  hover:scale-105 hover:bg-indigo-800 ">Filtrar</button>
                </div>
                <div className="justify-around flex flex-wrap">
                    {cards.length > 0 && cards.map((card) =>
                        <Card mass={card.initial_sample_mass} water={card.initial_water_mass} id={card.id} name={card.sample_name} data={card.finished_at} info={card}/>
                    )}
                </div>
            </div>
        </div>
    );
}
export default History;