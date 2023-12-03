from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import register_connection, set_default_connection

from ..settings import settings

AUTH_PROVIDER = PlainTextAuthProvider(
    username=settings.cassandra.USERNAME,
    password=settings.cassandra.PASSWORD,
)

cluster = Cluster(
    settings.cassandra.HOST,
    auth_provider=AUTH_PROVIDER,
)

session = cluster.connect(settings.cassandra.KEYSPACE)

register_connection(str(session), session=session)
set_default_connection(str(session))
