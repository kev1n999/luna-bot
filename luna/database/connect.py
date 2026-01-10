import pymongo 

# Function to connect with luna.db in MongoDB 
def lunaDatabase(mongo_uri: str):
  mongo_client = pymongo.MongoClient(mongo_uri)

  try:
    luna_db = mongo_client.get_database("luna")
    collection_names = luna_db.list_collection_names()

    print(f"Luna connected on {luna_db.name}")
    print(f"Luna.db Collections:\n{collection_names}\n")

    return luna_db 
  except Exception as err:
    print(err)