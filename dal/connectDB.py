import os

from pymongo import MongoClient,errors
from dotenv import load_dotenv

load_dotenv()

def connect_to_mongodb():
    try:
        mongo_uri = f'mongodb+srv://{os.getenv("ATLAS_USER")}:{os.getenv("ATLAS_USER_PASSWORD")}@devcluster.tlutfgy.mongodb.net/?retryWrites=true&w=majority&appName=DevCluster'
        client = MongoClient(mongo_uri)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except errors.ConnectionError as ce:
        print(f"Connection Error: {ce}")
        raise
    except errors.ConfigurationError as conf_err:
        print(f"Configuration Error: {conf_err}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

