from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


uri = os.getenv("URI")

client = MongoClient('mongodb://fam_db/myDB')

database = client.todo_db

try:
    client.admin.command('ping')
except Exception as e:
    print(e)

