from fastapi import APIRouter, status
from pydantic import BaseModel
from ..models.producto import Producto, Crear_producto, Borrar_producto
from ..database.connect import SessionDep


routes = APIRouter(prefix="/Productos", tags=["productos"])


@routes.get("")
async def ver_datos(sesion: SessionDep):
    return {"message": "Esto funciona"}


@routes.get("/{nombre}")
async def filtro_datos(sesion: SessionDep, nombre: str):

    return {"message": f"Producto encontrado con el nombre: {nombre}"}


@routes.post("/crear")
async def crear_datos(producto: Crear_producto, sesion: SessionDep) -> Producto:
    """
    Crea un nuevo producto.
    """
    nuevo_producto = Producto(**producto.model_dump())
    sesion.add(nuevo_producto)
    sesion.commit()
    sesion.refresh(nuevo_producto)
    return nuevo_producto





@routes.put("/actualizar")
async def actualiza_datos(producto: Crear_producto, sesion: SessionDep):
    """
    Updates an existing product in the database.  This is a placeholder and needs implementation.
    """
    return {"message": "Esto funciona"}


@routes.delete("/borrar")
async def borra_datos(producto: Borrar_producto, sesion: SessionDep):
    """
    Deletes a product from the database. This is a placeholder and needs implementation.
    """
    return {"message": "Esto funciona"}

