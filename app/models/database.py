from pymongo import MongoClient
from config import Config

db_client = MongoClient(Config.DATABASE_URI)


