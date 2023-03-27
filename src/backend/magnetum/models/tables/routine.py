from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from magnetum.models.tables.user import User

#from models.projetos import Projetos

class Routine(Base): #Estrutura para criar uma tabela
   __tablename__ = "routine"

   id= Column(Integer, primary_key=True, autoincrement=True)
   initiated_at=Column(DateTime, server_default=func.now())
   finished_at=Column(DateTime, server_default=func.now())
   sample_name=Column(String)
   initial_sample_mass=Column(Float)
   initial_water_mass=Column(Float)
   user_id = Column(Integer, ForeignKey('user.id'))
   project_id = Column(Integer, ForeignKey('project.id'))
   cycles = relationship('Cycle', backref='routine')
   
     
#    def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
#       return f"Cliente(id={self.id},numero_ciclo={self.numero_ciclo})"
      




