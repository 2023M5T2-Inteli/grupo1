# Código para conexão e configuração do banco de dados em SQLite, utilizando SQLAlchemy. O banco de dados é criado automaticamente caso não exista, e as tabelas são criadas caso não existam.

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from magnetum.models.tables.base import Base
from magnetum.models.tables.client import Client
from magnetum.models.tables.user import User
from magnetum.models.tables.project import Project
from magnetum.models.tables.cycle import Cycle
from magnetum.models.tables.routine import Routine

# Cria banco de dados caso ele não exista e estabelece conexão
engine = create_engine('sqlite+pysqlite:///app.db', echo=True)

# Estabelece sessão
Session = sessionmaker(bind=engine)
session = Session()

# Cria tabelas caso elas não existam
Base.metadata.create_all(engine) 

