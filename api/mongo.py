from pymongo import MongoClient

client = MongoClient() #default config

db = client['covid19_meta']