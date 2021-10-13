from sqlalchemy.orm import Session
from src.schema import schema
from src.infra.sqlalchemy.models import models

#


class RepositorioProduto():
    def __init__(self, db:Session=None):
        self.db = db

    def criar(self,produto: schema.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes= produto.detalhes,
                                    preco = produto.preco,
                                    disponivel = produto.disponivel,
                                    usuario_id = produto.usuario_id,
                                    tamanho = produto.tamanho)

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos
        """Outra forma de listar:----------
        -----------------------------------
        from sqlalchemy import select
        statement = select(models.Usuario)
        usuarios = self.session.execute(statement).all()
        return usuarios
        """

    def obter(self):pass

    def delete(self):pass