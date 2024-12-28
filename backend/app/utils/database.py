from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["story_app"]
collection = db["stories"]

def save_story(user_id, story):
    collection.insert_one({"user_id": user_id, "story": story})

def get_user_stories(user_id):
    return list(collection.find({"user_id": user_id}))
