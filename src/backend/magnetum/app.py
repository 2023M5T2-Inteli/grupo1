# Este é o código do servidor/backend do sistema, que intermedia as comunicações entre o usuário
# final na interface gráfica e o robô/microcontrolador. Essas comunicações se dão através de diferentes
# rotas de leitura e mudança de estados, que alteram variáveis globais e executam funções específicas
# em cada subsistema.

from flask import Flask, request
from flask_cors import CORS  # módulo para evitar erros de CORS
<<<<<<< HEAD
from magnetum.config import db
from magnetum.blueprints import routes
=======
from magnetum.blueprints import routes
#from magnetum.blueprints import routes1
from magnetum.routes import cliente
>>>>>>> af1f8d9f8507f868b5b017583ae77064278ef457

def create_app():
    app = Flask(__name__)  # Cria servidor
    db
    CORS(app)  # Adiciona proteção contra erros CORS
    routes.init_app(app)
<<<<<<< HEAD
=======
    #routes1.init_app(app)
    cliente.init_app(app)
>>>>>>> af1f8d9f8507f868b5b017583ae77064278ef457
    return app