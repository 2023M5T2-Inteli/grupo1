from magnetum.controllers import client
from flask import request

def init_app(app):
    @app.route('/client', methods=['GET'])
    def get_all():
        return client.get_all()

    @app.route('/client/<int:id>', methods=['GET'])
    def get_by_id(id):
        return client.get_by_id(id)

    @app.route('/client', methods=['POST'])
    def create():
        return client.create(request)

    @app.route('/client/<int:id>', methods=['PUT'])
    def update(id):
        return client.update(request, id)

    @app.route('/client/<int:id>', methods=['DELETE'])
    def delete(id):
        return client.delete(id)