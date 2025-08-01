from fastapi import FastAPI
from routers import productos

app = FastAPI()


app.include_router(productos.routes)


@app.get("/", tags=["index"])
async def root():
    return {"Hola que tal"}


