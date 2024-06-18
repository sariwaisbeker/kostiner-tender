from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://<userName>:<password>@<cluster>.mongodb.net/'

client = MongoClient(MONGO_URI)

db = client['<nameDB>']
