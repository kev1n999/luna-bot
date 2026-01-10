if __name__ == "__main__":
  import os 
  from .config.client import LunaClient
  from .config.constants import BOT_TOKEN, DEFAULT_PREFIX
  from .config.cogs import load_cogs
  from .config.messages import load_messages 
  from .config.luna_db import luna_db
  from .config.message_command import MessageCommandRegister

  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

  # Load message commands
  message_command_register = MessageCommandRegister()
  load_messages(ROOT_DIR, message_command_register)
  # Create the instance of the LunaClient 
  luna = LunaClient(bot_token=BOT_TOKEN, command_prefix=DEFAULT_PREFIX, message_commands=message_command_register)
  # Load cogs
  load_cogs(ROOT_DIR, luna.tree)
  # Start the luna
  luna.start_luna()