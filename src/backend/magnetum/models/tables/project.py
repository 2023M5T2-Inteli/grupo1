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

     def __repr__(self):
            return f"Project {self.name}, client: {self.client}, routines: {self.routines}"
     
     def return_json(self):
            return {
               "id": self.id,
               "name": self.name,
               "client": self.client.return_json(),
               "routines": [routine.return_json() for routine in self.routines]
            }