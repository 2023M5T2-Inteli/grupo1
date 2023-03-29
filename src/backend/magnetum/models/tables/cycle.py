# Definição da tabela ciclo

from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Cycle(Base): #Estrutura para criar uma tabela
   __tablename__ = "cycle"

   id= Column(Integer, primary_key=True, autoincrement=True)
   initiated_at=Column(DateTime, server_default=func.now())
   finished_at=Column(DateTime, server_default=func.now())
   magnet_intensity=Column(Integer)
   # Relacionamento com a tabela routine (many to one)
   routine_id = Column(Integer, ForeignKey('routine.id'))

   def __repr__(self):
      return f"Cycle {self.id}, initiated_at: {self.initiated_at}, finished_at: {self.finished_at}, magnet_intensity: {self.magnet_intensity}, routine_id: {self.routine_id}"
   
   def return_json(self):
      return {
         "id": self.id,
         "initiated_at": self.initiated_at,
         "finished_at": self.finished_at,
         "magnet_intensity": self.magnet_intensity,
         "routine_id": self.routine_id
      }
     
    
