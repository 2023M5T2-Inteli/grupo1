from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from base import Base
from magnetum.bluprints.models.pessoas import Pessoa


engine = create_engine('sqlite+pysqlite:///banco.db', echo=True)


#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

p1 = Pessoa(nome='Manu', idade=18, vampeta=False)
session.add(p1)
session.commit()

Base.metadata.create_all(engine) 