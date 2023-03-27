from flask import request 
from magnetum.controllers import routine

def init_app(app):
    @app.route('/current/tray', methods=['GET'])
    def get_tray():
        return routine.get_current_tray()

    @app.route('/current/tray', methods=['POST'])
    def set_tray():
        return routine.set_current_tray(request)

    