from magnetum.controllers import server
from flask import request

def init_app(app):
    @app.route('/server', methods=['GET'])
    def get_all_server():
        return server.get_all()
    
    @app.route('/server/<int:id>', methods=['GET'])
    def get_server_by_id(id):
        return server.get_by_id(id)
    
    @app.route('/server', methods=['POST'])
    def create_server():
        return server.create(request)
    
    @app.route('/server/<int:id>', methods=['PUT'])
    def update_server(id):
        return server.update(request, id)
    
    @app.route('/server/<int:id>', methods=['DELETE'])
    def delete_server(id):
        return server.delete(id)