import { useEffect } from 'react';

const serverHost = "http://127.0.0.1:5000";

function RangeSlider(props) {
    useEffect(() => {
        fetch('http://127.0.0.1:5000/current/magnet')
        .then((response) => {
            console.log(response)
            return response.json()
        })
        .then((data) => { 
            console.log(data)
            props.setValue(data['magnet_intensity'])
        });
    }, [])

    function changeIntensity(event) {
        props.setValue(Number.parseInt(event.target.value))
        fetch(serverHost + "/current/magnet", {
            method: "POST",
            body: JSON.stringify({
                magnet_intensity: Number.parseInt(event.target.value),
                magnet_state: props.state
            }),
            headers: { "Content-type": "application/json" },
        })
            .then((response) => {
                return response.json()
            })
            .then((data) => { console.log(data) });

    }
    return (
        <div className='flex justify-between'>
            <input type="range" min="0" max="12" step={1} value={props.value} onChange={(event) => changeIntensity(event)} />
            <p>{props.value} V</p>
        </div>
    );
}

export default RangeSlider