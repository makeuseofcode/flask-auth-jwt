from pymongo import MongoClient

def connect_to_mongodb(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client.get_database("users")
    return db
