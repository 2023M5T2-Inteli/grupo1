# cursor.execute("CREATE TABLE ciclo (    ciclo_id integer PRIMARY KEY, numero_ciclo INTEGER, massa_ciclo REAL NOT NULL);")

from magnetum.models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from typing import List
#from models.projetos import Projetos

class Ciclo(Base): #Estrutura para criar uma tabela
   __tablename__ = "ciclo"

   id= Column(Integer, primary_key=True, autoincrement=True)
   numero_ciclo= Column(String, nullable=False)
   massa_ciclo= Column(String, nullable=True)
   ensaios: Mapped[List["Ensaio"]] = relationship()
     
#    def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
#       return f"Cliente(id={self.id},numero_ciclo={self.numero_ciclo})"
      
    
