import MainCard from "../components/MainCard"
import Sidebar from "../components/Sidebar"
import startButton from '../assets/startButton.png'
import RangeSlider from 'react-range-slider-input';
import 'react-range-slider-input/dist/style.css';
import Input from "../components/Input";

function Home() {
    return (
        <div className="w-screen h-screen">
            <Sidebar />
            <div className="ml-20 h-screen flex items-start gap-15">
                <button><img src={startButton}/></button>
                <div>
                    <h1 className="text-3xl font-bold">Novo ensaio</h1>
                    <div>
                        <Input title='amostra'/>
                        <Input title='cliente'/>
                        <Input title='peso'/>
                        <Input title='data'/>
                        <Input title='horário'/>
                        <Input title='duração'/>
                    </div>
                    <div>
                        <RangeSlider />
                        <p>Ciclo</p>
                        <p>Status</p>
                    </div>

                </div>


            </div>
        </div>
    )
}

export default Home