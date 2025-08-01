from sqlmodel import SQLModel,Field



class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    precio: int | None = Field(default=None, index=True)
    descrpcion: str

class Insertar_producto(SQLModel, table=True):
    nombre: str = Field(index=True)
    precio: int | None = Field(default=None, index=True)
    descrpcion: str