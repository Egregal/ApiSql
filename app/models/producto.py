from pydantic import BaseModel
from sqlmodel import Field



class ProductoBase(BaseModel):
    id: int | None
    nombre: str
    precio: int | None
    descripcion: str

