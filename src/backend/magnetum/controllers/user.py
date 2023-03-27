# CRUD para tabela de usuários/técnicos

from magnetum.models.tables.user import User
from magnetum.config.db import session
from flask import request

# Retorna todos os usuários
def get_all():
    try:
        clients = session.query(User).all()
        return [client.return_json() for client in clients], 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Retorna usuário por id
def get_by_id(id):
    try:
        client = session.query(User).filter(User.id == id).first()
        return client.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Cria usuário com dados de request, em JSON    
def create(request):
    try:
        client = User(full_name=request.json['full_name'], cpf=request.json['cpf'])
        session.add(client)
        session.commit()
        return client.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Atualiza usuário com dados de request, em JSON
def update(request, id):
    try:
        client = session.query(User).filter(User.id == id).first()
        client.full_name = request.json['full_name']
        client.cpf = request.json['cpf']
        session.commit()
        return client.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Deleta usuário por id
def delete(id):
    try:
        client = session.query(User).filter(User.id == id).first()
        session.delete(client)
        session.commit()
        return {'status': 'success', 'message': 'client deleted'}, 204
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

