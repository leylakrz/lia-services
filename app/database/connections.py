import motor.motor_asyncio
from beanie import init_beanie

from app.models import Product
from settings import MONGODB_URL, MONGODB_DB


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    db = client.get_database(MONGODB_DB)
    await init_beanie(database=db, document_models=[Product])
