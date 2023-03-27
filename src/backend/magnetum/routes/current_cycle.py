from flask import request 
from magnetum.controllers import routine

def init_app(app):
    @app.route('/current/cycle', methods=['GET'])
    def get_cycle():
        return routine.get_current_cycle()
