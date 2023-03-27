from magnetum.models.tables.cycle import Cycle
from datetime import datetime
from magnetum.controllers.magnet import magnets

from flask import request

def get_all():
    try:
        cycles = Cycle.query.all()
        response = [cycle.return_json() for cycle in cycles]
        return response, 200

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def get_by_id(id):
    try:
        cycle = Cycle.query.filter(Cycle.id == id).first()
        return cycle.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def get_by_routine_id(id):
    try:
        cycles = Cycle.query.filter(Cycle.routine_id == id).all()
        response = [cycle.return_json() for cycle in cycles]
        return response, 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def create(request):
    try:
        cycle = Cycle(routine_id=request.json['routine_id'], initiated_at=datetime.now().isoformat(), magnet_intensity=magnets.get_intensity())
        cycle.save()
        return cycle.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def update(request, id):
    try:
        cycle = Cycle.query.filter(Cycle.id == id).first()
        cycle.finished_at = datetime.now().isoformat()
        cycle.save()
        return cycle.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def delete(id):
    try:
        cycle = Cycle.query.filter(Cycle.id == id).first()
        cycle.delete()
        return {'status': 'success', 'message': 'cycle deleted'}, 204
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500