# Definição da tabela user

from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base): #Estrutura para criar uma tabela
   __tablename__ = "user"

   id= Column(Integer, primary_key=True, autoincrement=True)
   cpf=Column(Integer)
   full_name=Column(String)
   # Relacionamento com a tabela routine (one to many)
   routines= relationship('Routine')

   def __repr__(self):
      return f"User {self.full_name}, CPF: {self.cpf}, routines: {self.routines}"

   def return_json(self):
      return {
         "id": self.id,
         "cpf": self.cpf,
         "full_name": self.full_name,
         "routines": [routine.return_json() for routine in self.routines]
      }
