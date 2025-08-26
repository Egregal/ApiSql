from pydantic import BaseModel
from sqlmodel import Field



class ProductoBase(BaseModel):
    nombre: str
    precio: float | None
    descripcion: str

class ProductoUpdate(BaseModel):
    id: int
    nombre:str

