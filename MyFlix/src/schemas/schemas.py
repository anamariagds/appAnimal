from pydantic import BaseModel
from typing import Optional


class serie(BaseModel):
    id: Optional[int] =  None
    titulo : str
    ano : int
    genero: str
    qtd_temporadas: int
    
    class Config:
        orm_mode = True