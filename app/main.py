from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
dataBase = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=dataBase)
session = Session()

Base = declarative_base()

class Usuario(Base):
    idUsuario = Column("idUsuario",Integer)
    nomeUsuario = Column("nomeUsuario",String)
    email = Column("email",String)
    senha = Column("senha",String)
    ativo = Column("ativo",Boolean)
class Livro(Base):
    idLivro =Column("idLivro",Integer)
    titulo = Column("titulo",String)
    qtdPaginas = Column("qtdPaginas",Integer)
    dono = Column("dono",ForeignKey("usuarios.idUsuario"))

Base.metadata.create_all(bind=dataBase)