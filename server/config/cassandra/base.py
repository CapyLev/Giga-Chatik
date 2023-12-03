from cassandra.cqlengine import models, columns
from config.settings import settings


class BaseModel(models.Model):
    __abstract__ = True
    __keyspace__ = settings.cassandra.CASSANDRA_KEYSPACE

    id = columns.UUID(primary_key=True)

    @classmethod
    def __tablename__(cls):
        return cls.__name__.lower()
