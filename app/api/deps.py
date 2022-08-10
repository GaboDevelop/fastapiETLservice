from typing import Generator
from app.database.mongo import Mongo

db = Mongo.initialize(
    Mongo,
    'mongodb+srv://gabodevelop:etlservice123@cluster0.5telvkv.mongodb.net/test',
    'etl_service'
)
def get_db() -> Generator:
    # try:
    return db
    # finally:
    #     print(db)
    #     db.close()
