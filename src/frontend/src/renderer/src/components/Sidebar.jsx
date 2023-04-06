import magnet from '../assets/sidebarMagnet.png'
import reports from '../assets/reportsIcon.png'
import plus from '../assets/plus.png'
import SidebarIcon from './SidebarIcon'

function Sidebar() {
    return (
        <div className="fixed h-screen bg-purple flex flex-col justify-between w-20 p-4">
            <div className='flex flex-col gap-6'>
                <SidebarIcon icon={magnet} title='Home' link='/'/>
                <SidebarIcon icon={reports} title='Histórico' link='/archive'/>
            </div>
            <SidebarIcon icon={plus} title='Adicionar' link='/profile'/>
        </div >
    )
}

export default Sidebar