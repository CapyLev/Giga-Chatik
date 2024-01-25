from celery import Celery


celery = Celery(
    "tasks",
    broker="pyamqp://guest:guest@localhost//",
    backend="rpc://",
)

celery.conf.update(
    timezone="UTC",
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)
