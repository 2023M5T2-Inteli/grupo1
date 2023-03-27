function Button(props) {
    return (
        <button className="bg-action text-primary my-2 w-60 rounded-lg p-2.5 text-sm shadow-sm shadow-current m-0 text-center" onClick={props.onClick}>{props.content}</button>
    )
}

export default Button