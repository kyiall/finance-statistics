from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

mongo_client = AsyncIOMotorClient(settings.DATABASE_URL)  # mongo_db название сервиса в композе
db = mongo_client["statistics_db"]
statistics_collection = db["statistics"]