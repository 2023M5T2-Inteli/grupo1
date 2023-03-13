import 'react-tooltip/dist/react-tooltip.css'
import { Tooltip } from 'react-tooltip'
import { useNavigate } from 'react-router-dom';

function SidebarIcon(props) {
    const navigate = useNavigate();
    return (
        <div className='group flex cursor-pointer' onClick={() => navigate(props.link)}>
            <img className="w-12 " src={props.icon} data-tooltip-id="my-tooltip" data-tooltip-content={props.title} data-tooltip-place='right'/>
            <Tooltip id="my-tooltip" style={{ backgroundColor: "#7758ef", color: "white" }}/>
        </div>
    );
}

export default SidebarIcon