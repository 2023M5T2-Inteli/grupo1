from magnetum.bluprints import robot
from enum import Enum
from flask import request 

# Enum para representar estados dos componentes
class State(Enum):
    ON = 1
    OFF = 0

    
# Declaração de variáveis globais
cycle_count = 0 # Contagem de ciclo atual do robô (quantas passadas ele já fez no ensaio atual)
magnet_state = State.OFF  
pump_state = State.OFF 

magnet_intensity = 12

current_tray = 0 # Bandeja atual do robô. Inicialmente, ele começa na bandeja 1.

# Número de passadas em cada ciclo. A ser dinamizado através das rotas nas próximas sprints.
cycles_per_trial = 5

def init_app(app):

    # CÓDIGO REFERENTE AO ROBÔ
    @app.route('/start_trial') 
    def start_trial():
        execute_trial()  
        return "Success", 200

    def execute_trial():
        restartCycleCount()  
        robot.rehome()  # Função do módulo do robô para levá-lo ao ponto neutro
        # Loop para realizar um número arbitrário de passadas.
        for i in range(cycles_per_trial):
            robot.execute_cycle()  
            incrementCycle()  
        global current_tray
        current_tray = 0

    @app.route('/cycleCount')  # Rota para ler número de ciclos (passadas) atual
    def getCycleCount():
        global cycle_count
        return ({"cycleCount": cycle_count})

    def restartCycleCount():
        global cycle_count
        cycle_count = 0

    def incrementCycle():
        global cycle_count  
        cycle_count = cycle_count + 1  

    # CÓDIGO PARA LER ESTADOS DO ÍMÃ E DA BOMBA
    # Rota para devolver estado do ímã e da bomba em JSON. Atualmente integrado
    # Rota para devolver estado do ímã e da bomba em JSON. Atualmente integrado apenas com o front, porque não descobrimos como processar JSON no Raspberry ainda
    @app.route('/states')
    def get_states():
        global magnet_state
        global pump_state
        return {"magnet": magnet_state.value, "pump": pump_state.value}

    # Rota que devolve apenas valor do estado do ímã para o Raspberry
    @app.route('/magnet_state')
    def get_magnet_state():
        global magnet_state
        return str(magnet_state.value)

    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/pump_state')
    def get_pump_state():
        global pump_state
        return str(pump_state.value)
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/current_tray')
    def get_current_tray():
        global current_tray
        return {'current_tray': current_tray}

    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/magnet_intensity')
    def get_magnet_intensity():
        global magnet_intensity
        return str(magnet_intensity)

    # CÓDIGO PARA MODIFICAR ESTADO DO ÍMÃ
    # Nesse caso, foi preciso separar as rotas das funções que modificam os valores, por serem variáveis
    # globais. Quando tentamos deixar tudo na mesma função da rota, o programa apresentava erros.

    # Esta rota recebe um JSON no body com chave "magnet_state" e valor booleano.
    @app.route('/toggle_magnet', methods=['POST'])
    def magnet():
        try:
            magnet_state = bool(request.json['magnet_state']) # Pega valor booleano do JSON
            if magnet_state == True: 
                enable_magnet()
                response = {'status': 'success', 'message': 'magnet enabled'}
            elif magnet_state == False:
                disable_magnet()
                response = {'status': 'success', 'message': 'magnet disabled'}
            else:
                response = {'status': 'error', 'message': 'invalid value for enable parameter'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response

    def disable_magnet():  
        global magnet_state
        magnet_state = State.OFF


    def enable_magnet():  
        global magnet_state
        magnet_state = State.ON

    # CÓDIGO PARA MODIFICAR ESTADO DA BOMBA
    # Nesse caso, foi preciso separar as rotas das funções que modificam os valores, por serem variáveis
    # globais. Quando tentamos deixar tudo na mesma função da rota, o programa apresentava erros.

    # Esta rota recebe um JSON no body com chave "pump_state" e valor booleano.
    @app.route('/toggle_pump', methods=['POST'])
    def pump():
        try:
            pump_state = bool(request.json['pump_state']) # Pega valor booleano do JSON
            if pump_state == True:
                enable_pump()
                response = {'status': 'success', 'message': 'pump on'}
            elif pump_state == False:
                disable_pump()
                response = {'status': 'success', 'message': 'pump off'}
            else:
                response = {'status': 'error', 'message': 'invalid value'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response

    def disable_pump():  
        global pump_state
        pump_state = State.OFF


    def enable_pump():  
        global pump_state
        pump_state = State.OFF

    @app.route('/change_tray', methods=['POST'])
    def tray():
        try:
            global current_tray
            json_input = int(request.json['current_tray']) # Pega valor booleano do JSON
            if json_input in [0, 1, 2, 3]:
                current_tray = json_input
                response = {'status': 'success', 'message': 'tray changed'}
            else:
                response = {'status': 'error', 'message': 'invalid value for tray parameter'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response


    @app.route('/change_magnet_intensity', methods=['POST'])
    def magnet_intensity():
        try:
            global magnet_intensity
            json_input = int(request.json['magnet_intensity']) # Pega valor booleano do JSON
            if json_input in range(0, 13):
                magnet_intensity = json_input
                print(magnet_intensity)
                response = {'status': 'success', 'message': 'intensity changed'}
            else:
                response = {'status': 'error', 'message': 'invalid value for tray parameter'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response
