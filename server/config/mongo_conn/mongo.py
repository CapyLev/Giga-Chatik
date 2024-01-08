from typing import Any, Dict, List
from motor.motor_asyncio import AsyncIOMotorClient

from ..settings import settings


class MongoCollection(object):
    def __init__(self) -> None:
        self.connection = AsyncIOMotorClient(settings.mongo.MONGO_URL)

    @property
    def collection(self) -> AsyncIOMotorClient:
        return self.connection[settings.mongo.NAME][settings.mongo.COLLECTION]

    def insert(self, document) -> None:
        self.collection.insert_one(document)

    def update(self, document: Dict[Any, Any]) -> None:
        self.collection.update_one(
            {"_id": document.id}, {"$set": document}, upsert=True
        )

    def insert_many(self, documents: List[Dict[Any, Any]]) -> None:
        bulk = self.collection.initialize_unordered_bulk_op()
        for document in documents:
            bulk.insert(document)
        bulk.execute()

    def update_many(self, documents: List[Dict[Any, Any]]) -> None:
        bulk = self.collection.initialize_unordered_bulk_op()
        for document in documents:
            bulk.find({"_id": document.id}).upsert().update_one({"$set": document})
        bulk.execute()

    def _find_by_ids(self, ids: List[str]) -> Dict[Any, Any]:
        return self.collection.find({"_id": {"$in": ids}})
