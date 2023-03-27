from magnetum.models.tables.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class User(Base): #Estrutura para criar uma tabela
   __tablename__ = "user"

   id= Column(Integer, primary_key=True, autoincrement=True)
   cpf=Column(Integer)
   full_name=Column(String)
   routines= relationship('Routine', backref='user')
