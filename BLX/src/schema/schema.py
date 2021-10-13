from pydantic import BaseModel
from typing import Optional, List

#modelos request/ parte externa
### necessario sub classe Config em todas as classes!

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    ##produtos : List[produtos] = []

    class Config:
        orm_mode = True
  
class Produto(BaseModel):
    id : Optional[int] = None
    nome: str
    detalhes : str
    preco : float
    disponivel : Optional[bool] = False
    tamanho : str
    usuario_id: int
    usuario: Optional[Usuario]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id : Optional[int] = None
    
    quantidade : int
    entrega : bool = True
    endereco : str
    observacoes : Optional[str] = 'Sem Observações'

