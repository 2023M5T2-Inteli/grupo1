from magnetum.models import robot
from magnetum.utils.Tray import Tray
cycles_per_trial = 5

# Contagem de ciclo atual do robô (quantas passadas ele já fez no ensaio atual)
cycle_count = 0

current_tray = Tray.CAPTURA


def execute_routine():
    restartCycleCount()
    robot.rehome()  # Função do módulo do robô para levá-lo ao ponto neutro
    # Loop para realizar um número arbitrário de passadas.
    for i in range(cycles_per_trial):
        robot.execute_cycle()
        incrementCycle()
    global current_tray
    current_tray = 0
    return "Success", 200


def restartCycleCount():
    global cycle_count
    cycle_count = 0


def incrementCycle():
    global cycle_count
    cycle_count = cycle_count + 1


def get_current_cycle():
    global cycle_count
    response = {"cycleCount": str(cycle_count)}
    return response, 200


def get_current_tray():
    global current_tray
    response = {'current_tray': str(current_tray)}
    return response, 200


def set_current_tray(request):
    try:
        global current_tray
        new_tray = request.json['current_tray']
        if new_tray in [1, 2, 3]:
            current_tray = Tray(new_tray)
            response = {'status': 'success', 'message': 'tray changed'}
        else:
            response = {'status': 'error',
                        'message': 'invalid value for tray parameter'}
        return response, 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
