import pymongo 

# Function to connect with luna.db in MongoDB 
def lunaDatabase(mongo_uri: str) -> pymongo.database.Database | None:
  # Instancce of the pymongo client
  mongo_client = pymongo.MongoClient(mongo_uri)

  try:
    # Get the luna database 
    luna_db = mongo_client.get_database("luna")
    # Get the list of collections in luna database
    collection_names = luna_db.list_collection_names()

    print(f"Luna connected on {luna_db.name}")
    print(f"Luna.db Collections:\n{collection_names}\n")

    return luna_db 
  except Exception as err:
    print(err)