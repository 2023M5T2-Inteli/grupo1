import { useState } from 'react';

const serverHost = "http://10.128.0.159:5000";


function RangeSlider() {
    const [value, setValue] = useState(0);

    function changeIntensity(event) {
        setValue(event.target.value)
        fetch(serverHost + "/change_magnet_intensity", {
            method: "POST",
            body: JSON.stringify({
                magnet_intensity: event.target.value,
            }),
            headers: { "Content-type": "application/json;charset=UTF-8" },
        })
            .then((response) => {
                response.json()
            })
            .then((data) => { console.log(data) });

    }
    return (
        <div className='flex justify-between'>
            <input type="range" min="0" max="12" step={1} value={value} onChange={(event) => changeIntensity(event)} />
            <p>{value} V</p>
        </div>
    );
}

export default RangeSlider