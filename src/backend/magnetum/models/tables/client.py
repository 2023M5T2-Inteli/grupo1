from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Client(Base): #Estrutura para criar uma tabela
   __tablename__ = "client"

   id= Column(Integer, primary_key=True, autoincrement=True)
   full_name= Column(String, nullable=False)
   cnpj=Column(Integer)
   projects = relationship('Project', backref='client')

   def __repr__(self):
      return f"Client {self.full_name}, CNPJ: {self.cnpj}, project: {self.projects}"

   def return_json(self):
      return {
         "id": self.id,
         "full_name": self.full_name,
         "cnpj": self.cnpj,
      }
      
    
