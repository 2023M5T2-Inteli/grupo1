from magnetum.controllers import user
from flask import request

def init_app(app):
    @app.route('/user', methods=['GET'])
    def get_all_users():
        return user.get_all()

    @app.route('/user/<int:id>', methods=['GET'])
    def get_user_by_id(id):
        return user.get_by_id(id)

    @app.route('/user', methods=['POST'])
    def create_user():
        return user.create(request)

    @app.route('/user/<int:id>', methods=['PUT'])
    def update_user(id):
        return user.update(request, id)

    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        return user.delete(id)