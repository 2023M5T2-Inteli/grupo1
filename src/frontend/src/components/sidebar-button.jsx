function sidebarButton(props) {
    return (
        <div className="p-2.5 flex items-center rounded-md px-4 duration-300 cursor-pointer bg-white text-white">
            <i className="bi bi-house-door-fill"></i>
            <span className="text-[15px] ml-4 text-gray-200 font-bold">{props.content}</span>
        </div>
    )
}

export default sidebarButton