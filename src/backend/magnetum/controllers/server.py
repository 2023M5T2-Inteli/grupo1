from magnetum.models.tables.server import Server
from magnetum.config.db import session
from flask import request

def get_all():
    try:
        servers = session.query(Server).all()
        return [server.return_json() for server in servers], 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
    
def get_by_id(id):
    try:
        server = session.query(Server).filter(Server.id == id).first()
        return server.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500
    
def create(request):
    try:
        server = Server(name=request.json['name'], ip=request.json['ip'], port=request.json['port'])
        session.add(server)
        session.commit()
        return server.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def update(request, id):
    try:
        server = session.query(Server).filter(Server.id == id).first()
        server.name = request.json['name']
        server.ip = request.json['ip']
        server.port = request.json['port']
        session.commit()
        return server.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

def delete(id):
    try:
        server = session.query(Server).filter(Server.id == id).first()
        session.delete(server)
        session.commit()
        return 'Success', 204
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500