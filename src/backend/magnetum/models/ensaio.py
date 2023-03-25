from magnetum.models.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

#from models.projetos import Projetos

class Ensaio(Base): #Estrutura para criar uma tabela
   __tablename__ = "ensaio"

   id= Column(Integer, primary_key=True, autoincrement=True)
   data= Column(String)
   hora= Column(String)
   operador= Column(String)
   duracao= Column(String)
   massa_solido= Column(Float)
   massa_agua= Column(Float)
   cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))
   ciclo_id: Mapped[int] = mapped_column(ForeignKey("ciclo.id"))
   
     
#    def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
#       return f"Cliente(id={self.id},numero_ciclo={self.numero_ciclo})"
      




