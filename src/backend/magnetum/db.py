from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.cliente import Cliente
from models.projetos import Projetos

engine = create_engine('sqlite+pysqlite:///banco.db', echo=True)


#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 

projetos = Projetos(nome_projeto='Meu projeto', cliente_id=1)
#print(cliente)
session.add(projetos)
session.commit()