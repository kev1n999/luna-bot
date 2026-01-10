if __name__ == "__main__":
  import os 
  from .config.client import LunaClient
  from .config.constants import BOT_TOKEN
  from .config.cogs import load_cogs
  from .config.luna_db import luna_db
  
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

  # Create the instance of the LunaClient 
  luna = LunaClient(bot_token=BOT_TOKEN)
  # Load cogs
  load_cogs(ROOT_DIR, luna.tree)
  # Start the luna
  luna.start_luna()