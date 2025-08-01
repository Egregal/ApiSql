from pydantic import BaseModel
from sqlmodel import Field


class Producto(BaseModel):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    precio: int | None = Field(default=None, index=True)
    descrpcion: str

class Crear_producto(BaseModel):
    nombre: str = Field(index=True)
    precio: int | None = Field(default=None, index=True)

class Borrar_producto(BaseModel):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
