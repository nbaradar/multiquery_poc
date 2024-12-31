from pymongo import MongoClient

def store_result_in_mongodb(uri: str, db_name: str, collection_name: str, data: dict):
    """
    Stores a JSON result into a MongoDB collection.

    :param uri: MongoDB connection URI.
    :param db_name: Name of the database.
    :param collection_name: Name of the collection.
    :param data: The JSON result to store.
    """
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    try:
        result = collection.insert_one(data)
        print(f"Result successfully stored in MongoDB with ID: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred while storing the result in MongoDB: {str(e)}")
    finally:
        client.close()
