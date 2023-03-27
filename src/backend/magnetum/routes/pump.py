# Rotas para estado da bomba

from magnetum.controllers import pump
from flask import request

def init_app(app):
    @app.route('/current/pump', methods=['POST'])
    def set_current_pump():
        return pump.set_current(request)
    
    @app.route('/current/pump', methods=['GET'])
    def get_current_pump():
        return pump.get_current()