from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship

### modelo no banco de dados 
#### MODELO ORM



class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    user_produtos = relationship('Produto', back_populates='usuario')


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanho = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))

    usuario = relationship('Usuario', back_populates='user_produtos')