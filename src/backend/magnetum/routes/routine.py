from flask import request 
from magnetum.controllers import routine


def init_app(app):
    @app.route('/routine', methods=['GET'])
    def get_all():
        return routine.get_all()

    @app.route('/routine/<int:id>', methods=['GET'])
    def get_by_id(id):
        return routine.get_by_id(id)

    @app.route('/routine/start', methods=['GET'])
    def start():
        return routine.execute_routine(request)

    @app.route('/routine/<int:id>', methods=['PUT'])
    def update(id):
        return routine.update(request, id)

    @app.route('/routine/<int:id>', methods=['DELETE'])
    def delete(id):
        return routine.delete(id)
   