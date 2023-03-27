from magnetum.controllers import user

def init_app(app):
    @app.route('/user', methods=['GET'])
    def get_all():
        return user.get_all()

    @app.route('/user/<int:id>', methods=['GET'])
    def get_by_id(id):
        return user.get_by_id(id)

    @app.route('/user', methods=['POST'])
    def create():
        return user.create(request)

    @app.route('/user/<int:id>', methods=['PUT'])
    def update(id):
        return user.update(request, id)

    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete(id):
        return user.delete(id)