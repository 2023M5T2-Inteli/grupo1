from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from magnetum.models.base import Base
<<<<<<<< HEAD:src/backend/magnetum/config/db.py
<<<<<<<< HEAD:src/backend/magnetum/config/db.py
from models.cliente import Cliente
from models.projetos import Projetos
from models.ciclo import Ciclo
from models.ensaio import Ensaio
========
========
>>>>>>>> af1f8d9f8507f868b5b017583ae77064278ef457:src/backend/magnetum/models/db.py
from magnetum.models.cliente import Cliente
from magnetum.models.projetos import Projetos
from magnetum.models.ciclo import Ciclo
from magnetum.models.ensaio import Ensaio
<<<<<<<< HEAD:src/backend/magnetum/config/db.py
>>>>>>>> af1f8d9f8507f868b5b017583ae77064278ef457:src/backend/magnetum/models/db.py
========
>>>>>>>> af1f8d9f8507f868b5b017583ae77064278ef457:src/backend/magnetum/models/db.py

engine = create_engine('sqlite+pysqlite:///banco.db', echo=True)

#Cria uma sessão para conversar com banco de dados (SQLite no caso)
Session = sessionmaker(bind=engine)
session = Session()

#Cria as tabelas se elas não existirem
Base.metadata.create_all(engine) 

# projetos = Cliente(nome='Manuu')
# session.add(projetos)
# session.commit()