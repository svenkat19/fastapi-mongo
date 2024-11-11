
from pymongo import MongoClient


client=MongoClient("mongodb+srv://svenkat:svenkat@books-store-mern.qzdblbr.mongodb.net/?retryWrites=true&w=majority&appName=Books-Store-MERN"
)

db=client.todo_db
collection_name=db["todo_collection"]
