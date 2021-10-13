from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schema import schema
from src.infra.sqlalchemy.repositorios import repositorio_Produto, repositorio_Usuario
from typing import List


#   START SERVE ==>                        uvicorn src.server:app --reload --reload-dir=src
#   ativar ambiente virtual                .\env1\Scripts\Activate.ps1

criar_db()

app = FastAPI()

@app.get('/')
def home():
    return {'PAGINA INICIAL':'OK-SUCCES'}

#PRODUTOS ---------------------------------------------------------------------------------------------------------

@app.post('/produtos',  status_code=status.HTTP_201_CREATED, response_model=schema.Produto)
def criar_produto(produto: schema.Produto, db: Session = Depends(get_db)):
    produto_criado = repositorio_Produto.RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model= List[schema.Produto])
def listar_produtos(db: Session =Depends(get_db)):
    produtos = repositorio_Produto.RepositorioProduto(db).listar()
    return produtos
#---------------------------------------------------------------------------------------------------------



#USUÁRIOS---------------------------------------------------------------------------------------------------------
@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schema.Usuario)
def criar_usuario(usuario:schema.Usuario, db:Session=Depends(get_db)):
    usuario_criado = repositorio_Usuario.RepositorioUsuario(db).criar(usuario)
    return usuario_criado 
 
@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[schema.Usuario])
def list_User(db: Session = Depends(get_db)):
    usuarios = repositorio_Usuario.RepositorioUsuario(db).listar()
    return usuarios




#---------------------------------------------------------------------------------------------------------------------------------------