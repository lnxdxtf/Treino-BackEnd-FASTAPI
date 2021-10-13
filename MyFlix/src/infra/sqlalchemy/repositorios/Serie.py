from sqlalchemy.orm import Session
from src.schemas.schema_1 import Serie
from src.infra.sqlalchemy.models import models
from sqlalchemy import select,delete

class SerieRepositiorio():
    def __init__(self, db:  Session=None):
        self.db = db

    def create(self, serie:Serie):
        db_serie = models.Serie(titulo=serie.titulo,
                                ano=serie.ano,
                                genero=serie.genero,
                                qtd_temporadas=serie.qtd_temporadas)
                    
        self.db.add(db_serie)
        self.db.commit()            #<<<---- commit confirma a transação no db
        self.db.refresh(db_serie)
    
    def list(self):
        series_db = self.db.query(models.Serie).all()
        return series_db

    def show(self, serie_id:int):
        statement = select(models.Serie).filter_by(id=serie_id)
        serie_by_id = self.db.execute(statement).one()
        return serie_by_id

    def delete(self, serie_id:int):
        statement = delete(models.Serie).where(models.Serie.id == serie_id)
        self.db.execute(statement)
        self.db.commit()