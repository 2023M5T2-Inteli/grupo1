from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String

class Server(Base): #Estrutura para criar uma tabela
    __tablename__ = "server"

    id= Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String)
    ip=Column(String)
    port=Column(Integer)

    def __repr__(self):
        return f"Server {self.id}, name: {self.name}, ip: {self.ip}, port: {self.port}"
    
    def return_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "ip": self.ip,
            "port": self.port
        }
    