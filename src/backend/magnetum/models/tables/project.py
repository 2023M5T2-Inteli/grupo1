from magnetum.models.tables.base import Base
from magnetum.models.tables.client import Client
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Project(Base): #Estrutura para criar uma tabela
     __tablename__ = "project"

     id= Column(Integer, primary_key=True, autoincrement=True)
     name= Column(String, nullable=False)
     client_id = Column(Integer, ForeignKey('client.id'))
     routines = relationship('Routine', backref='project')
