from magnetum.extentions.base import Base
from sqlalchemy import Column, Integer, String, Boolean

class Pessoa(Base): #Estrutura para criar uma tabela
     __tablename__ = "pessoas"
     id= Column(Integer, primary_key=True)
     nome= Column(String)
     idade= Column(Integer)
     vampeta= Column(Boolean)

     def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
        return f"Pessoa(id={self.id}, nome={self.nome}, idade={self.idade}, gosta do vampeta={self.vampeta})"
     
