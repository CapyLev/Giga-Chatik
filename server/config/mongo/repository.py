from typing import Any, Dict, List
from motor.motor_asyncio import AsyncIOMotorClient

from ..settings import settings


class BaseMongoRepository:
    def __init__(self) -> None:
        self.connection = AsyncIOMotorClient(settings.mongo.MONGO_URL)

    @property
    def collection(self) -> AsyncIOMotorClient:
        return self.connection[settings.mongo.NAME][settings.mongo.COLLECTION]

    def insert(self, document: Dict[Any, Any]) -> None:
        self.collection.insert_one(document)

    def update(self, document: Dict[Any, Any]) -> None:
        self.collection.update_one(
            {"_id": document["_id"]}, {"$set": document}, upsert=True
        )

    def insert_many(self, documents: List[Dict[Any, Any]]) -> None:
        self.collection.insert_many(documents)

    def update_many(self, documents: List[Dict[Any, Any]]) -> None:
        for document in documents:
            self.collection.update_one(
                {"_id": document["_id"]}, {"$set": document}, upsert=True
            )

    def find_by_ids(self, ids: List[str]) -> List[Dict[Any, Any]]:
        return list(self.collection.find({"_id": {"$in": ids}}))
