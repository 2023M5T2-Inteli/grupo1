from magnetum.models import robot
from magnetum.utils.Tray import Tray
from magnetum.models.tables.routine import Routine
from datetime import datetime
from magnetum.config.db import session


cycles_per_trial = 5

# Contagem de ciclo atual do robô (quantas passadas ele já fez no ensaio atual)
cycle_count = 0

current_tray = Tray.CAPTURA

def get_all():
    try:
        routines = session.query(Routine).all()
        response = [routine.return_json() for routine in routines]
        return response, 200

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def get_by_id(id):
    try:
        routines = session.query(Routine).filter(Routine.id == id).first()
        return routines.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
    
def create(new_routine):
    try:
        routine = Routine(name=new_routine['name'], client_id=new_routine['client_id'], initiated_at=datetime.now().isoformat(), sample_name=new_routine['sample_name'], initial_sample_mass=new_routine['initial_sample_mass'], initial_water_mass=new_routine['initial_water_mass'], user_id=new_routine['user_id'], project_id=new_routine['project_id'])
        session.add(routine)
        session.commit()
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def update(request, id):
    try:
        routine = session.query(Routine).filter(Routine.id == id).first()
        routine.name = request.json['name']
        routine.client_id = request.json['client_id']
        routine.sample_name = request.json['sample_name']
        routine.initial_sample_mass = request.json['initial_sample_mass']
        routine.initial_water_mass = request.json['initial_water_mass']
        routine.initiated_at = request.json['initiated_at']
        routine.finished_at = request.json['finished_at']
        routine.user_id = request.json['user_id']
        routine.project_id = request.json['project_id']
        session.commit()
        return routine.return_json().id
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def finish(id):
    try:
        routine = session.query(Routine).filter(Routine.id == id).first()
        routine.finished_at = datetime.now().isoformat()
        session.commit()
        return routine.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def delete(id):
    try:
        routine = session.query(Routine).filter(Routine.id == id).first()
        session.delete(routine)
        session.commit()
        return {'status': 'success', 'message': 'routine deleted'}, 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def execute_routine(request):
    routine = {
        'name': request.json['name'],
        'client_id': request.json['client_id'],
        'sample_name': request.json['sample_name'],
        'initial_sample_mass': request.json['initial_sample_mass'],
        'initial_water_mass': request.json['initial_water_mass'],
        'user_id': request.json['user_id'],
        'project_id': request.json['project_id']

    }
    id = create(routine)
    restartCycleCount()
    #robot.rehome()  # Função do módulo do robô para levá-lo ao ponto neutro
    # Loop para realizar um número arbitrário de passadas.
    for i in range(cycles_per_trial):
        #robot.execute_cycle()
        incrementCycle()
    finish(id)
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