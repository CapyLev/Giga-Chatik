from motor.motor_asyncio import AsyncIOMotorClient

from ..settings import settings


class MongoDBConnector:
    _client = None
    _database = None
    _collection = None

    async def init_mongo_db(self) -> None:
        self._client = AsyncIOMotorClient(settings.mongo.MONGO_URL)
        self._database = self._client[settings.mongo.NAME]
        self._collection = self._database[settings.mongo.COLLECTION]

        await self._create_database_if_not_exist()
        await self._create_collection_if_not_exists()
        await self._create_index()

    async def _create_database_if_not_exist(self) -> None:
        if settings.mongo.NAME not in await self._client.list_database_names():
            await self._client.admin.command("create", settings.mongo.NAME)

    async def _create_collection_if_not_exists(self) -> None:
        if (
            settings.mongo.COLLECTION
            not in await self._database.list_collection_names()
        ):
            await self._database.create_collection(settings.mongo.COLLECTION)

    async def _create_index(self) -> None:
        await self._collection.create_index([("chat_id", 1), ("timestamp", 1)])
        await self._collection.create_index([("chat_id", 1), ("user_id", 1)])


mongo_db_connection: MongoDBConnector = MongoDBConnector()
