from magnetum.services import pump

@app.route('/pump', methods=['POST'])
def pump():
    try:
        new_pump_state = bool(request.json['pump_state']) # Pega valor booleano do JSON
        if pump_state == True:
            enable_pump()
            response = {'status': 'success', 'message': 'pump on'}
        elif pump_state == False:
            disable_pump()
            response = {'status': 'success', 'message': 'pump off'}
        else:
            response = {'status': 'error', 'message': 'invalid value'}
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
    return response