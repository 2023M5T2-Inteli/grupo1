from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.cliente import Cliente
from models.projetos import Projetos
from models.ciclo import Ciclo
from models.ensaio import Ensaio

engine = create_engine('sqlite+pysqlite:///banco.db', echo=True)

#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 

# projetos = Cliente(nome='Manuu')
# session.add(projetos)
# session.commit()