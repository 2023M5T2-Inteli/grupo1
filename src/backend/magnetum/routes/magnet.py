from flask import request 
from magnetum.controllers import magnet

def init_app(app):
    
    # Esta rota recebe um JSON no body com chave "magnet_state" e valor booleano.
    @app.route('/current/magnet', methods=['POST'])
    def set_current_magnet():
        return magnet.set_current(request)
    
    @app.route('/current/magnet', methods=['GET'])
    def get_current_magnet():
        return magnet.get_current()
        

    
    
    