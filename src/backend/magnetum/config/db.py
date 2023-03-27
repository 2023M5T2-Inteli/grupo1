from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from magnetum.models.tables.base import Base


engine = create_engine('sqlite+pysqlite:///app.db', echo=True)

#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 
