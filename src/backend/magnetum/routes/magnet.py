from flask import request 
from magnetum.controllers import magnet
import traceback

def init_app(app):
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/magnet/intensity')
    def get_current_magnet_intensity():
        global magnet_intensity
        return str(magnet_intensity)
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/magnet/intensity/json')
    def get_current_json_magnet_intensity():
        global magnet_intensity
        return {"magnet_intensity": magnet_intensity}
    
    # Esta rota recebe um JSON no body com chave "magnet_state" e valor booleano.
    @app.route('/magnet', methods=['POST'])
    def change_magnet():
        try:
            magnet_state = bool(request.json['magnet_state']) # Pega valor booleano do JSON
            if magnet_state == True: 
                magnet.enable_magnet()
                response = {'status': 'success', 'message': 'magnet enabled'}
            elif magnet_state == False:
                magnet.disable_magnet()
                response = {'status': 'success', 'message': 'magnet disabled'}
            else:
                response = {'status': 'error', 'message': 'invalid value for enable parameter'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response
    
    @app.route('/current/magnet', methods=['GET'])
    def get_current_magnet():
        return magnet.get_current()
        

    
    
    