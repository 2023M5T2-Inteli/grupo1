from models.base import Base
from sqlalchemy import Column, Integer


class Ciclo(Base): #Estrutura para criar uma tabela
   __tablename__ = "ciclo"

   id= Column(Integer, primary_key=True, autoincrement=True)
   numero_ciclo= Column(Integer, nullable=False)
   
     
   def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
      return f"Cliente(id={self.id},numero_ciclo={self.numero_ciclo})"
      
