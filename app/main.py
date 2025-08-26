from fastapi import FastAPI
from routers import productos
from sqlmodel import SQLModel
from database.connect import engine
from database.model import Productos

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(productos.routes)


@app.get("/", tags=["index"])
async def root():
    return {"Hola que tal"}


