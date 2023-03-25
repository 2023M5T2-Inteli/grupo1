from flask import request 
from routes import magnet
def init_app(app):
    
    @app.route('/magnet/state')
    def get_magnet_state():
        global magnet_state
        return str(magnet_state.value)
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/magnet/intensity')
    def get_magnet_intensity():
        global magnet_intensity
        return str(magnet_intensity)
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/magnet/intensity/json')
    def get_json_magnet_intensity():
        global magnet_intensity
        return {"magnet_intensity": magnet_intensity}
    
    # Esta rota recebe um JSON no body com chave "magnet_state" e valor booleano.
    @app.route('/magnet', methods=['POST'])
    def magnet():
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
    
    @app.route('/magnet', methods=['GET'])
    def magnet():
        try:
            magnet_state = magnet.state_magnet # Pega valor booleano do JSON
            response = {'status': 'error', 'message': magnet_state}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response

    
    
    