from flask import request 
from magnetum.models.client import Client
from magnetum.models import db


def init_app(app):

    # CÓDIGO REFERENTE AO ROBÔ
    @app.route('/novo_cliente', methods=['POST']) 
    def novo_cliente():
        db
        client_name = Cliente(nome=request.json["nome"])
        db.session.add(client_name)
        db.session.commit()
        return "Sucess", 200
    
    @app.route('/clientes') 
    def cliente():
        db
        clientes = db.session.query(Cliente).all()
        return [cliente.return_json() for cliente in clientes]
    
    
    
   
