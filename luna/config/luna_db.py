from .constants import MONGO_URI
from luna.database.connect import lunaDatabase

# Connection with luna.db
luna_db = lunaDatabase(MONGO_URI)