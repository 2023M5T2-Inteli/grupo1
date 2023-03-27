import capitalizeFirstLetter from "../utils/strings"
import { useFormContext } from "react-hook-form";

function Input(props) {
    const { register } = useFormContext();
    return (
        <div className="my-2">
            <label className='font-bold font-montserrat' htmlFor={props.title}>{capitalizeFirstLetter(props.title) + ':'}</label>
            <input className="ml-3 border-b border-b-purple outline-0 w-auto font-montserrat" name={props.title} type={props.type} {...register(props.title)}/>
        </div>
    )
}

export default Input