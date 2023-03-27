from magnetum.controllers import project
from flask import request

def init_app(app):
    @app.route('/project')
    def get_all_projects():
        return project.get_all()

    @app.route('/project/<int:id>')
    def get_project_by_id(id):
        return project.get_by_id(id)

    @app.route('/project', methods=['POST'])
    def create_project():
        return project.create(request)

    @app.route('/project/<int:id>', methods=['PUT'])
    def update_project(id):
        return project.update(request, id)

    @app.route('/project/<int:id>', methods=['DELETE'])
    def delete_project(id):
        return project.delete(id)