from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from typing import List
#from models.projetos import Projetos

class Client(Base): #Estrutura para criar uma tabela
   __tablename__ = "client"

   id= Column(Integer, primary_key=True, autoincrement=True)
   full_name= Column(String, nullable=False)
   cnpj=Column(Integer)
   projects = relationship('Project', backref='client')
      
    
