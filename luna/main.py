if __name__ == "__main__":
  from .config.client import LunaClient
  from .config.constants import BOT_TOKEN

  # Create the instance of the LunaClient 
  luna = LunaClient(bot_token=BOT_TOKEN)
  # Start the luna
  luna.start_luna()