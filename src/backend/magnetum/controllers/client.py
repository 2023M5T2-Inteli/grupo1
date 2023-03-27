# Funções para interação (CRUD) com tabela de clientes

from magnetum.models.tables.client import Client
from magnetum.config.db import session

# Pegar todos os clientes
def get_all():
    try:
        clients = session.query(Client).all()
        return [client.return_json() for client in clients], 200 
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Pegar cliente por id
def get_by_id(id):
    try:
        client = session.query(Client).filter(Client.id == id).first()
        return client.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Criar cliente com dados de request, em JSON
def create(request):
    try:
        client = Client(full_name=request.json['full_name'], cnpj=request.json['cnpj'])
        session.add(client)
        session.commit()
        return client.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Atualizar cliente com dados de request, em JSON
def update(request, id):
    try:
        client = session.query(Client).filter(Client.id == id).first()
        client.full_name = request.json['full_name']
        client.cnpj = request.json['cnpj']
        session.commit()
        return client.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Deletar cliente por id
def delete(id):
    try:
        client = session.query(Client).filter(Client.id == id).first()
        session.delete(client)
        session.commit()
        return {'status': 'success', 'message': 'client deleted'}, 204
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500


