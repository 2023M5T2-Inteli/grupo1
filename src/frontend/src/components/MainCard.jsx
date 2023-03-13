import startButton from '../assets/startButton.png'
function MainCard() {
    return (
        <div className="flex">
            <button><img src={startButton}/></button>
            <h1 className="text-3xl font-bold">Novo ensaio</h1>
        </div>
    )
}

export default MainCard