from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

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
   
     
   def __repr__(self):
      return f"Routine {self.id}, initiated_at: {self.initiated_at}, finished_at: {self.finished_at}, sample_name: {self.sample_name}, initial_sample_mass: {self.initial_sample_mass}, initial_water_mass: {self.initial_water_mass}, user_id: {self.user_id}, project_id: {self.project_id}, cycles: {self.cycles}"

   def return_json(self):
      return {
         "id": self.id,
         "initiated_at": self.initiated_at,
         "finished_at": self.finished_at,
         "sample_name": self.sample_name,
         "initial_sample_mass": self.initial_sample_mass,
         "initial_water_mass": self.initial_water_mass,
         "user_id": self.user_id,
         "project_id": self.project_id,
         "cycles": [cycle.return_json() for cycle in self.cycles]
      }



