# cursor.execute("CREATE TABLE ciclo (    ciclo_id integer PRIMARY KEY, numero_ciclo INTEGER, massa_ciclo REAL NOT NULL);")

from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, relationship
from typing import List
#from models.projetos import Projetos

class Cycle(Base): #Estrutura para criar uma tabela
   __tablename__ = "cycle"

   id= Column(Integer, primary_key=True, autoincrement=True)
   initiated_at=Column(DateTime, server_default=func.now())
   finished_at=Column(DateTime, server_default=func.now())
   magnet_intensity=Column(Integer)
   routine_id = Column(Integer, ForeignKey('routine.id'))
     
    
