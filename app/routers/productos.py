from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select
from database.model import Productos
from models.producto import ProductoBase, ProductoUpdate
from database.connect import SessionDep
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


routes = APIRouter(prefix="/productos", tags=["productos"])


async def get_producto_or_404(producto_id: int, sesion: SessionDep) -> Productos:
    producto = sesion.get(Productos, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@routes.get("")
async def ver_datos(sesion: SessionDep):
    """
    Recibe todos los productos de la bbdd
    """

    result = sesion.exec(select(Productos)).all()
    return result


@routes.get("/{nombre}")
async def filtro_datos(sesion: SessionDep, nombre: str):
    """
    Recibe producto por filtrado por nombre
    """
    producto = sesion.exec(select(Productos).where(Productos.nombre == nombre)).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@routes.post("/crear")
async def crear_datos(producto: ProductoBase, sesion: SessionDep):
    """
    Crea un nuevo producto en la bbdd.

    """
    nuevo_producto = Productos.model_validate(producto)
    sesion.add(nuevo_producto)
    sesion.commit()
    sesion.refresh(nuevo_producto)
    return nuevo_producto


@routes.put("/actualizar/{producto_name}")
async def actualiza_datos(
    producto: ProductoUpdate,
    sesion: SessionDep,

    db_producto: Annotated[Productos, Depends(get_producto_or_404)],
):
    producto_data = producto.model_dump(exclude_unset=True)
    for key, value in producto_data.items():
        setattr(db_producto, key, value)
    sesion.add(db_producto)
    sesion.commit()
    sesion.refresh(db_producto)
    return db_producto


@routes.delete("/borrar/{producto_id}")
async def borra_datos(
    sesion: SessionDep,
    db_producto: Annotated[Productos, Depends(get_producto_or_404)],
    token: Annotated[str, Depends(oauth2_scheme)],
):
    sesion.delete(db_producto)
    sesion.commit()
    return {"message": "Producto borrado"}




