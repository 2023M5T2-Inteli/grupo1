import Sidebar from "../components/Sidebar"
import startButton from '../assets/startButton.png'
import RangeSlider from 'react-range-slider-input';
import 'react-range-slider-input/dist/style.css';
import Input from "../components/Input";
import pumpIcon from '../assets/pumpIcon.png'
import turnOnIcon from '../assets/turnOnIcon.png'
import magnetIcon from '../assets/sidebarMagnet.png'
import { useRef, useState } from "react";
import seeMore from '../assets/seeMoreArrow.png'




function Home() {
    const [intensity, setIntensity] = useState([0, 12])
    const [cycle, setCycle] = useState(0)
    const [status, setStatus] = useState(0)
    const detailsRef = useRef();

    function showDetails() {
        detailsRef.current.scrollIntoView();
    }

    return (
        <div className="w-full h-screen">
            <Sidebar />
            <div className="ml-20 flex flex-col items-center justify-center">
                <div className="flex h-screen items-center gap-10 justify-center">
                    <button><img className="hover:scale-105" src={startButton} /></button>
                    <div>
                        <h1 className="text-3xl font-bold mb-5">Novo ensaio</h1>
                        <div className="flex">
                            <div className="pr-5 pl-2 flex flex-col justify-between">
                                <p className="text-slate-500 small-caps">INFORMAÇÕES</p>
                                <Input title='amostra' />
                                <Input title='cliente' />
                                <Input title='peso' />
                                <Input title='data' />
                                <Input title='horário' />
                                <Input title='duração' />
                            </div >
                            <div id='sliderWrapper' className="pr-5 pl-2 w-96 flex flex-col justify-between gap-4">
                                <p className="text-slate-500 small-caps">CONTROLES</p>

                                <span className="flex gap-5 justify-around">
                                    <button><img className="w-9" src={turnOnIcon}></img></button>
                                    <button><img className="w-9" src={magnetIcon}></img></button>
                                    <button><img className="w-9" src={pumpIcon}></img></button>
                                </span>
                                <p className="font-bold">Intensidade do ímã: </p>
                                <span className="flex gap-2 items-center justify-center">
                                    <RangeSlider min={0} max={12} thumbsDisabled={[true, false]} value={intensity} onInput={setIntensity} />
                                    <p>{intensity[1] + 'V'}</p>
                                </span>
                                <span className="flex gap-2">
                                    <p className="font-bold">Ciclo: </p>
                                    <p>Nº DE CICLOS</p>
                                </span>
                                <span className="flex gap-2">
                                    <p className="font-bold">Status: </p>
                                    <p>BANDEJA ATUAL</p>
                                </span>
                            </div>
                        </div>
                    </div>

                </div>
                <button className="w-14 absolute bottom-5 flex justify-center" onClick={showDetails}>
                    <img src={seeMore} />
                </button>
                <div className="w-[90%] h-96 bg-white rounded-xl shadow-2xl m-5 flex justify-center items-center" ref={detailsRef}>
                    MAIS INFORMAÇÕES
                </div>
            </div>
        </div>
    )
}

export default Home