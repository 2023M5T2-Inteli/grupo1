# CRUD para tabela de projetos

from magnetum.config.db import session
from magnetum.models.tables.project import Project

# Pegar todos os projetos
def get_all():
    try:
        projects = session.query(Project).all()
        return [project.return_json() for project in projects], 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Pegar projeto por id
def get_by_id(id):
    try:
        project = session.query(Project).filter(Project.id == id).first()
        return project.return_json(), 200
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Criar projeto com dados de request, em JSON
def create(request):
    try:
        project = Project(name=request.json['name'], client_id=request.json['client_id'])
        session.add(project)
        session.commit()
        return project.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Atualizar projeto com dados de request, em JSON
def update(request, id):
    try:
        project = session.query(Project).filter(Project.id == id).first()
        project.name = request.json['name']
        project.client_id = request.json['client_id']
        session.commit()
        return project.return_json(), 201
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500

# Deletar projeto por id
def delete(id):
    try:
        project = session.query(Project).filter(Project.id == id).first()
        session.delete(project)
        session.commit()
        return 'Success', 204
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return response, 500