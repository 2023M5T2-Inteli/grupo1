# Rotas para estado do ímã

from flask import request 
from magnetum.controllers import magnet

def init_app(app):
    
    @app.route('/current/magnet', methods=['POST'])
    def set_current_magnet():
        return magnet.set_current(request)
    
    @app.route('/current/magnet', methods=['GET'])
    def get_current_magnet():
        return magnet.get_current()
        

    
    
    