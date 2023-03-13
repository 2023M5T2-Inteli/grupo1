import capitalizeFirstLetter from "../utils/strings"

function Input(props) {
    return (
        <div>
            <label for={props.title}>{capitalizeFirstLetter(props.title) + ':'}</label>
            <input className="ml-3 border-b border-b-purple outline-0" name={props.title} type="text"/>
        </div>
    )
}

export default Input