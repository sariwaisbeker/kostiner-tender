import json
import os

from pymongo import errors
from dotenv import load_dotenv

from CreateDB.connectDB import connect_to_mongodb

load_dotenv()

mongo_uri = f'mongodb+srv://{os.getenv("ATLAS_USER")}:{os.getenv("ATLAS_USER_PASSWORD")}@devcluster.tlutfgy.mongodb.net/?retryWrites=true&w=majority&appName=DevCluster'

# יצירת חיבור ל-MongoDB Atlas


# שם מסד הנתונים והאוספים
db_name = os.getenv("DATABASE_NAME")
collections = json.loads(os.getenv("COLLECTIONS"))

def create_database_and_collections(client, db_name, collections):
    db = client[db_name]
    for collection_name in collections:
        if collection_name in db.list_collection_names():
            print(f"האוסף '{collection_name}' כבר קיים.")
        else:
            try:
                print(f"יצירת האוסף '{collection_name}'...")
                db.create_collection(collection_name)
            except errors.CollectionInvalid as ci:
                print(f"Collection Error: {ci}")
                raise
            except Exception as e:
                print(f"An error occurred while creating collection '{collection_name}': {e}")
                raise
    print(f"מסד הנתונים '{db_name}' והאוספים נוצרו בהצלחה.")

def main():
    # חיבור ל-MongoDB Atlas
    client = connect_to_mongodb(mongo_uri)

    # שם מסד הנתונים והאוספים
    db_name = os.getenv("DATABASE_NAME")
    collections = json.loads(os.getenv("COLLECTIONS"))

    # בדיקת קיום מסד הנתונים והאוספים
    try:
        if db_name in client.list_database_names():
            print(f"המסד נתונים '{db_name}' כבר קיים.")
            db = client[db_name]
            create_database_and_collections(client, db_name, collections)
        else:
            print(f"יצירת מסד נתונים '{db_name}'...")
            create_database_and_collections(client, db_name, collections)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        # סגירת החיבור ל-MongoDB
        client.close()

if __name__ == "__main__":
    main()

