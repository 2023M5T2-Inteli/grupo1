# CRUD para tabela de ensaios
from magnetum.models import robot
from magnetum.utils.Tray import Tray
from magnetum.models.tables.routine import Routine
from datetime import datetime
from magnetum.config.db import session
from magnetum.controllers import cycle

# Quantidade de ciclos que o robô deve fazer em cada ensaio (a ser dinamizado)
cycles_per_trial = 5

# Contagem de ciclo atual do robô (quantas passadas ele já fez no ensaio atual)
cycle_count = 0

# Bandeja atual do robô (onde ele está)
current_tray = Tray.DESATIVADO

# Pega todos os ensaios
def get_all():
    try:
        routines = session.query(Routine).all()
        response = [routine.return_json() for routine in routines]
        return response, 200

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Pega ensaio por id
def get_by_id(id):
    try:
        routines = session.query(Routine).filter(Routine.id == id).first()
        return routines.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Cria ensaio com dados de request, em JSON 
def create(new_routine):
    try:
        routine = Routine(initiated_at=datetime.now(), sample_name=new_routine['sample_name'], initial_sample_mass=new_routine['initial_sample_mass'], initial_water_mass=new_routine['initial_water_mass'], user_id=new_routine['user_id'], project_id=new_routine['project_id'])
        session.add(routine)
        session.commit()
        return routine.id
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Atualiza ensaio com dados de request, em JSON
def update(request, id):
    try:
        routine = session.query(Routine).filter(Routine.id == id).first()
        routine.sample_name = request.json['sample_name']
        routine.initial_sample_mass = request.json['initial_sample_mass']
        routine.initial_water_mass = request.json['initial_water_mass']
        routine.user_id = request.json['user_id']
        routine.project_id = request.json['project_id']
        session.commit()
        return routine.return_json()
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Finaliza ensaio, atualizando o campo finished_at
def finish(id):
    try:
        routine = session.query(Routine).filter(Routine.id == id).first()
        routine.finished_at = datetime.now()
        session.commit()
        return routine.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Deleta ensaio
def delete(id):
    try:
        routine = session.query(Routine).filter(Routine.id == id).first()
        session.delete(routine)
        session.commit()
        return {'status': 'success', 'message': 'routine deleted'}, 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 204

# Executa ensaio, chamando o robô para realizar o número de ciclos definido e criando o ensaio no banco de dados
def execute_routine(request):
    routine = {
        'sample_name': request.json['sample_name'],
        'initial_sample_mass': request.json['initial_sample_mass'],
        'initial_water_mass': request.json['initial_water_mass'],
        'user_id': request.json['user_id'],
        'project_id': request.json['project_id'],
        
    }
    id = create(routine)

    restartCycleCount()
    robot.rehome()  # Função do módulo do robô para levá-lo ao ponto neutro

    # # Loop para realizar um número arbitrário de passadas.
    for i in range(int(request.json['cycleCount'])):

        robot.execute_cycle(12)
        cycle.create(id)
        incrementCycle()

    finish(id)

    # Reseta bandejas
    global current_tray
    current_tray = Tray.DESATIVADO

    restartCycleCount()

    return {"routine_id": id}, 200

# Funções para modificar variável global de ciclo
def restartCycleCount():
    global cycle_count
    cycle_count = 0

def incrementCycle():
    global cycle_count
    cycle_count = cycle_count + 1

# Função para retornar variável global de ciclo
def get_current_cycle():
    global cycle_count
    response = {"cycleCount": str(cycle_count)}
    return response, 200

# Função para retornar variável global de bandeja
def get_current_tray():
    global current_tray
    response = {'current_tray': str(current_tray.value)}
    return response, 200

# Função para modificar variável global de bandeja
def set_current_tray(request):
    try:
        global current_tray
        new_tray = request.json['current_tray']
        if new_tray in [1, 2, 3]: # Valores possíveis de bandeja
            current_tray = Tray(new_tray)
            response = {'status': 'success', 'message': 'tray changed'}
        else: # Caso o valor de bandeja seja inválido
            response = {'status': 'error',
                        'message': 'invalid value for tray parameter'}
        return response, 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500