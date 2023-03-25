from magnetum.models.base import Base
from magnetum.models.cliente import Cliente
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Projetos(Base): #Estrutura para criar uma tabela
     __tablename__ = "projetos"
     id= Column(Integer, primary_key=True, autoincrement=True)
     nome_projeto= Column(String, nullable=False)
     cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"))
     
     def __repr__(self) -> str: #Serve para formatar o objeto que vai aparecer ao printar um objeto pessoa 
          return f"Projetos(id={self.id},numero_projetos={self.numero_projetos},cliente_id={self.cliente_id})"