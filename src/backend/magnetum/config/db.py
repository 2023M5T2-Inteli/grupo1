from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from magnetum.models.tables.base import Base
from magnetum.models.tables.client import Client
from magnetum.models.tables.project import Project
from magnetum.models.tables.cycle import Cycle
from magnetum.models.tables.routine import Routine

engine = create_engine('sqlite+pysqlite:///app.db', echo=True)

#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 

projetos = Client(full_name='Manuu')
session.add(projetos)
session.commit()