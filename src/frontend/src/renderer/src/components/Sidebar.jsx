import magnet from '../assets/sidebarMagnet.png'
import reports from '../assets/reportsIcon.png'
import profile from '../assets/profileIcon.png'
import demo from '../assets/demoIcon.png'
import SidebarIcon from './SidebarIcon'

function Sidebar() {
    return (
        <div className="fixed h-screen bg-purple flex flex-col justify-between w-20 p-4">
            <div className='flex flex-col gap-6'>
                <SidebarIcon icon={magnet} title='Home' link='/'/>
                <SidebarIcon icon={reports} title='Reports' link='/archive'/>
                <SidebarIcon icon={demo} title='Demo' link='/demo'/>
                <SidebarIcon icon={demo} title='Server' link='/server'/>
            </div>
            <SidebarIcon icon={profile} title='Profile' link='/profile'/>
        </div >
    )
}

export default Sidebar