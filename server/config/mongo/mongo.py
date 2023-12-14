from motor.motor_asyncio import AsyncIOMotorClient

from ..settings import settings

mongo_client = AsyncIOMotorClient(settings.mongo.MONGO_URL)
mongo_db = mongo_client[settings.mongo.NAME]
