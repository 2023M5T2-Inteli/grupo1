import magnet from '../assets/magnet.png'

function Sidebar(props) {
    return (
    <>
        <div className="sidebar flex-1 min-height-screen p-2 col-span-2 overflow-y-auto text-center bg-gray-900">
            <div className="text-gray-100 text-xl">
                <div className="p-2.5 mt-1 flex items-center">
                    <img className="p-2 w-[40px] ml-2" src={magnet}/>
                    <h1 className="font-bold text-gray-200 text-[18px] ml-2">Tectonics</h1>
                    <i className="bi bi-x cursor-pointer ml-28 lg:hidden"></i>
                </div>
            <div className="my-2 bg-gray-600 h-[1px]"></div>
            </div>

            <div className="p-2.5 flex items-center rounded-md px-4 duration-300 cursor-pointer bg-gray-900 hover:bg-blue-600 text-white">
                <i className="bi bi-house-door-fill"></i>
                <span className='font-bold ml-2 bg-gray-900 text-[18px]'>Home</span>
            </div>

            <div className="p-2.5 flex items-center rounded-md px-4 duration-300 cursor-pointer bg-gray-900 hover:bg-blue-600 text-white">
                <i className="bi bi-house-door-fill"></i>
                <span className='font-bold ml-2 bg-gray-900 text-[18px]'>Histórico</span>
            </div>

            <div className="my-4 bg-gray-600 h-[1px]"></div>

            <div className="p-2.5 mt-3 flex items-center rounded-md px-4 duration-300 cursor-pointer hover:bg-blue-600 text-white">
                <i className="bi bi-box-arrow-in-right"></i>
                <span className="font-bold ml-2 bg-gray-900 text-[18px]">Logout</span>
            </div>

        </div>
    </>
    )
}

export default Sidebar