import os
from pymongo import MongoClient

MONGO_URI = os.environ["MONGO_URI"]    # Secret Manager injects this
DB_NAME = "reddit_data"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
