import capitalizeFirstLetter from "../utils/strings"

function Input(props) {
    return (
        <div className="my-2">
            <label className='font-bold' htmlFor={props.title}>{capitalizeFirstLetter(props.title) + ':'}</label>
            <input className="ml-3 border-b border-b-purple outline-0 w-auto" name={props.title} type="text"/>
        </div>
    )
}

export default Input