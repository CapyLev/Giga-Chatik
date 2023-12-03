from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from ..settings import settings


auth_provider = PlainTextAuthProvider(
    username=settings.cassandra.CASSANDRA_USERNAME,
    password=settings.cassandra.CASSANDRA_PASSWORD,
)

cluster = Cluster(
    [f"{settings.cassandra.CASSANDRA_HOST}:{settings.cassandra.CASSANDRA_PORT}"],
)

session = cluster.connect(settings.cassandra.CASSANDRA_KEYSPACE)
