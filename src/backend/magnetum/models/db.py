from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from magnetum.models.base import Base
from magnetum.models.cliente import Cliente
from magnetum.models.projetos import Projetos
from magnetum.models.ciclo import Ciclo
from magnetum.models.ensaio import Ensaio

engine = create_engine('sqlite+pysqlite:///banco.db', echo=True)

#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 

projetos = Cliente(nome='Manuu')
session.add(projetos)
session.commit()