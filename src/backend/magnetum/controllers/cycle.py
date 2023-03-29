# Funções para interação (CRUD) com tabela de ciclos

from magnetum.models.tables.cycle import Cycle
from datetime import datetime
from magnetum.controllers.magnet import magnets
from magnetum.config.db import session

from flask import request

# Pegar todos os ciclos
def get_all():
    try:
        cycles = session.query(Cycle).all()
        return [cycle.return_json() for cycle in cycles], 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Pegar ciclo por id
def get_by_id(id):
    try:
        cycle = session.query(Cycle).filter(Cycle.id == id).first()
        return cycle.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Criar ciclo com dados de request, em JSON
def create(routine_id):
    try:
        cycle = Cycle(routine_id=routine_id, magnet_intensity=magnets.get_intensity())
        session.add(cycle)
        session.commit()
        return cycle.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Deletar ciclo por id
def delete(id):
    try:
        cycle = session.query(Cycle).filter(Cycle.id == id).first()
        session.delete(cycle)
        session.commit()
        return {'status': 'success', 'message': 'Cycle deleted'}, 204
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500