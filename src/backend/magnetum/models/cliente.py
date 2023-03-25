from magnetum.models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from typing import List
#from models.projetos import Projetos

class Cliente(Base): #Estrutura para criar uma tabela
   __tablename__ = "cliente"

   id= Column(Integer, primary_key=True, autoincrement=True)
   nome= Column(String, nullable=False)
   projetos: Mapped[List["Projetos"]] = relationship()
   ensaios: Mapped[List["Ensaio"]] = relationship()
     
   def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
      return f"Cliente(id={self.id},numero_ciclo={self.nome})"
   
   def return_json(self):
      return {"id":self.id,"nome":self.nome}
      
    
