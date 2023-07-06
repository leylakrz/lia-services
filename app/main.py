from fastapi import FastAPI

from app.database.connections import init_db
from app.routers import product_router

app = FastAPI(title="Product")


@app.on_event("startup")
async def start_db():
    await init_db()


app.include_router(product_router)
