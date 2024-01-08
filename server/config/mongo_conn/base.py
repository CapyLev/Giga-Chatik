from mongoengine import Document


class BaseDocument(Document):
    meta = {
        "auto_create_index": False,
        "abstract": True,
    }
