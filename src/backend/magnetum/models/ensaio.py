# cursor.execute("CREATE TABLE ensaio (   ensaio_id integer PRIMARY KEY
# , cliente_id,
# data text NOT NULL, hora REAL NOT NULL, operador text NOT NULL, duracao REAL NOT NULL, massa_solido REAL NOT NULL, massa_agua REAL NOT NULL, campo REAL NOT NULL, ciclo_id);")

from models.base import Base
from sqlalchemy import Column, Integer, Text, DateTime, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

#from models.projetos import Projetos

class Ensaio(Base): #Estrutura para criar uma tabela
   __tablename__ = "ensaio"

   id= Column(Integer, primary_key=True, autoincrement=True)
   cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))
   ciclo_id: Mapped[int] = mapped_column(ForeignKey("ciclo.id"))
   data= Column(String)
   hora= Column(String)
   operador= Column(String)
   duracao= Column(String)
   massa_solido= Column(Float)
   massa_agua= Column(Float)
   
     
#    def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
#       return f"Cliente(id={self.id},numero_ciclo={self.numero_ciclo})"
      




