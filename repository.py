from config import database
from bson import ObjectId


class CollectionRepo():
    def __init__(self, collection: str, _id: str = None, _json=None):
        self.collection = database[collection]
        self._id = _id
        self._json = _json

    def list(self):
        items = []
        for item in self.collection.find():
            item['_id'] = str(item['_id'])
            items.append(item)
        return items

    def create(self):
        item = self._json
        self.collection.insert_one(item)
        item["_id"] = str(item["_id"])
        return item

    def update(self):
        item = self.collection.update_one({'_id': ObjectId(self._id)}, {"$set": self._json})

    def detail(self):
        try:
            item = self.collection.find_one({"_id": ObjectId(self._id)})
            item["_id"] = str(item["_id"])
            return item
        except:
            return []

    def delete(self):
        self.collection.delete_one({'_id': ObjectId(self._id)})
