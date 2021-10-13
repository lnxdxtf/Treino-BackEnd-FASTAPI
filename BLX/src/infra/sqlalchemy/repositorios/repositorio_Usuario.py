from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schema import schema
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():

    def __init__(self, db:Session=None):
        self.db= db


    def criar(self, usuario: schema.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    telefone=usuario.telefone,
                                    senha = usuario.senha)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
        
    def listar(self):
        statement = select(models.Usuario)
        usuarios = self.db.execute(statement).scalars().all()
        return usuarios

        # usuarios = self.db.query(models.Usuario).all()
        # return usuarios

        """Outra forma de listar:----------
        -----------------------------------
        from sqlalchemy import select
        statement = select(models.Usuario)
        usuarios = self.session.execute(statement).all()
        return usuarios
        """
    def obter(self):pass
    def delete(self):pass