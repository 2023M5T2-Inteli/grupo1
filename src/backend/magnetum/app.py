# Este é o código do servidor/backend do sistema, que intermedia as comunicações entre o usuário
# final na interface gráfica e o robô/microcontrolador. Essas comunicações se dão através de diferentes
# rotas de leitura e mudança de estados, que alteram variáveis globais e executam funções específicas
# em cada subsistema.

from flask import Flask
from flask_cors import CORS  # módulo para evitar erros de CORS
from magnetum.routes import magnet, pump, routine, client, user, project, cycle, tray, server, current_cycle # Rotas
from magnetum.config import db # Configurações do banco de dados

def create_app():
    app = Flask(__name__)  # Cria servidor
    CORS(app)  # Adiciona proteção contra erros CORS
    db # Inicializa banco de dados

    # Inicializa rotas
    magnet.init_app(app)
    pump.init_app(app)
    routine.init_app(app)
    client.init_app(app)
    user.init_app(app)
    project.init_app(app)
    cycle.init_app(app)
    tray.init_app(app)
    current_cycle.init_app(app)
    
    return app