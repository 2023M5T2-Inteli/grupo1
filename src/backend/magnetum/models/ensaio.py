# cursor.execute("CREATE TABLE ensaio (   ensaio_id integer PRIMARY KEY
# , cliente_id,
# data text NOT NULL, hora REAL NOT NULL, operador text NOT NULL, duracao REAL NOT NULL, massa_solido REAL NOT NULL, massa_agua REAL NOT NULL, campo REAL NOT NULL, ciclo_id);")

from models.base import Base
from sqlalchemy import Column, Integer, Text, DateTime, String, Float

#from models.projetos import Projetos

class Ciclo(Base): #Estrutura para criar uma tabela
   __tablename__ = "ciclo"

   id= Column(Integer, primary_key=True, autoincrement=True)
   numero_ciclo= Column(Integer, nullable=False)
   data = Column(DateTime, nullable=True)
   hora = Column(DateTime, nullable=True)
   operador = Column(String, nullable=True)
   duracao = Column(String, nullable=True)
   massa_solida = Column(Float, nullable=True)
   massa_agua = Column(Float, nullable=True)
    #campo = Column(String, nullable=True)
   
     
#    def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
#       return f"Cliente(id={self.id},numero_ciclo={self.numero_ciclo})"
      




