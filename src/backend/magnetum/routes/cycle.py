from magnetum.controllers import cycle
from flask import request
def init_app(app):

    @app.route('/cycle', methods=['GET'])
    def get_all():
        return cycle.get_all()

    @app.route('/cycle/<int:id>', methods=['GET'])
    def get_by_id(id):
        return cycle.get_by_id(id)

    @app.route('/cycle', methods=['POST'])
    def create():
        return cycle.create(request)

    @app.route('/cycle/<int:id>', methods=['PUT'])
    def update(id):
        return cycle.update(request, id)

    @app.route('/cycle/<int:id>', methods=['DELETE'])
    def delete(id):
        return cycle.delete(id)
