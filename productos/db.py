from django.conf import settings
from pymongo import MongoClient


if not settings.MONGO_URI:
    raise RuntimeError(
        "MONGO_URI=mongodb+srv://abrahamlacruz79_db_user:1077483140@cluster0.kkdshyj.mongodb.net/"
    )


cliente = MongoClient(
    settings.MONGO_URI,
    serverSelectionTimeoutMS=5000
)

db = cliente[settings.MONGO_DB]

coleccion_productos = db["productos"]