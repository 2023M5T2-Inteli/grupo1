# Definição da tabela cliente

from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Client(Base): #Estrutura para criar uma tabela
   __tablename__ = "client"

   id= Column(Integer, primary_key=True, autoincrement=True)
   full_name= Column(String, nullable=False)
   cnpj=Column(Integer)
   # Relacionamento com a tabela project (one to many)
   projects = relationship('Project')

   def __repr__(self):
      return f"Client {self.full_name}, CNPJ: {self.cnpj}, project: {self.projects}"

   def return_json(self):
      print(self.projects)
      return {
         "id": self.id,
         "full_name": self.full_name,
         "cnpj": self.cnpj,
         "projects": [project.return_json() for project in self.projects]
      }
      
    
