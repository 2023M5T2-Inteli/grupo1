from flask import request 
# from magnetum.models import cliente
from magnetum.models import db
def init_app(app):

    # CÓDIGO REFERENTE AO ROBÔ
    @app.route('/novo_cliente', methods=['POST']) 
    def novo_cliente():
        
        
        # xcliente = cliente.Cliente(nome='Henrique Marlon')
        # db.session.add(xcliente)
        # db.session.commit()
        return "deu certo olhe só"
   
