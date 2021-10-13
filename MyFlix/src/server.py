from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schema_1 import Serie
from src.infra.sqlalchemy.repositorios.Serie import SerieRepositiorio

#   START SERVE ==>                        uvicorn src.server:myFlix --reload --reload-dir=src
#   ativar ambiente virtual                .\myFlix-ENV\Scripts\Activate.ps1

criar_db()

myFlix = FastAPI()

#add uma serie
@myFlix.post('/series')
def add_serie(serie:Serie, db: Session=Depends(get_db)):
    serie_added = SerieRepositiorio(db).create(serie)
    msg_post = {"serie":"adicionada"}
    return msg_post,serie_added
''
#mostra todas as series
@myFlix.get('/series')
def show_series(db:Session=Depends(get_db)):
    series = SerieRepositiorio(db).list()
    return series

#mostra a serie por id
@myFlix.get('/series/{serie_id}')
def show_serie(serie_id:int,db: Session = Depends(get_db)):     #TODAS AS ROTAS PRECISAM DECLARAR O BANCO DE DADOS,
    serie_show_by_id = SerieRepositiorio(db).show(serie_id)     #NO CASO: db: Session = Depends(get_db)
    return serie_show_by_id

@myFlix.delete('/series/{serie_id}')
def delete_serie(serie_id, db: Session = Depends(get_db)):
    msg_delete = {f"Série: {serie_id}":" deletada"}
    SerieRepositiorio(db).delete(serie_id)
    return msg_delete