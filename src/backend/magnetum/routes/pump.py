from magnetum.services import pump
from flask import request

def init_app(app):
    @app.route('/pump', methods=['POST'])
    def change_pump_state():
        try:
            new_pump_state = bool(request.json['pump_state']) # Pega valor booleano do JSON
            if new_pump_state == True:
                pump.enable_pump()
                response = {'status': 'success', 'message': 'pump on'}
            elif new_pump_state == False:
                pump.disable_pump()
                response = {'status': 'success', 'message': 'pump off'}
            else:
                response = {'status': 'error', 'message': 'invalid value'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response
    
    @app.route('/pump', methods=['GET'])
    def get_pump_state():
        try:
            pump_state = pump.pump_state
            response = {'status': 'success', 'pump_state': pump_state}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response