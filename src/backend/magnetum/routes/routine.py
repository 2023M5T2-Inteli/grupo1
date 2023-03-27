from flask import request 
from magnetum.controllers import routine


def init_app(app):

    # CÓDIGO REFERENTE AO ROBÔ
    @app.route('/routine/start') 
    def start_routine():
        routine.execute_routine()  

    @app.route('/current/cycle')  # Rota para ler número de ciclos (passadas) atual
    def get_current_cycle():
        return routine.get_current_cycle()
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/current/tray')
    def get_current_tray():
        return routine.get_current_tray()
    
    @app.route('/current/tray', methods=['POST'])
    def set_current_tray():
        return routine.set_current_tray(request)
   