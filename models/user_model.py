from pymongo.collection import Collection
from bson.objectid import ObjectId


class User:
    def __init__(self, collection: Collection, username: str, password: str):
        self.collection = collection
        self.username = username
        self.password = password

    def save(self):
        user_data = {
            'username': self.username,
            'password': self.password
        }
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def find_by_id(collection: Collection, user_id: str):
        return collection.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def find_by_username(collection: Collection, username: str):
        return collection.find_one({'username': username})
