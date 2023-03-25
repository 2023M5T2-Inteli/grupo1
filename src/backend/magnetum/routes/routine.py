from flask import request 
from magnetum.services import routine

def init_app(app):

    # CÓDIGO REFERENTE AO ROBÔ
    @app.route('/routine/start') 
    def start_trial():
        routine.execute_trial()  
        return "Success", 200 

    @app.route('/routine/cycle_count')  # Rota para ler número de ciclos (passadas) atual
    def getCycleCount():
        return ({"cycleCount": str(routine.getCurrentCycle())})
   