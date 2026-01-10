import os 
from dotenv import load_dotenv 

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
DEFAULT_PREFIX = "lu!"
MONGO_URI = os.getenv("MONGO_URI")
GOOGLE_GENAI_KEY = os.getenv("GOOGLE_GENAI_KEY")