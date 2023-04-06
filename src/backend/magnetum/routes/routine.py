
# Rotas para ensaios (tabela)

from flask import request 
from magnetum.controllers import routine


def init_app(app):
    @app.route('/routine', methods=['GET'])
    def get_all_routines():
        return routine.get_all()

    @app.route('/routine/<int:id>', methods=['GET'])
    def get_routine_by_id(id):
        return routine.get_by_id(id)
    
    # Inicia ensaio e salva no banco de dados
    @app.route('/routine', methods=['POST'])
    def start_routine():
        print('start routine')
        return routine.execute_routine(request)

    @app.route('/routine/<int:id>', methods=['PUT'])
    def update_routine(id):
        return routine.update(request, id)

    @app.route('/routine/<int:id>', methods=['DELETE'])
    def delete_routine(id):
        return routine.delete(id)
   