from sqlmodel import SQLModel,Field



class Productos(SQLModel):
    id: int | None = Field(primary_key=True)
    nombre: str
    precio: int | None
    descripcion: str

