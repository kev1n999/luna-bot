import discord 
from discord import app_commands 

class LunaClient(discord.Client):
  def __init__(self, bot_token: str):
    super().__init__(
      intents=discord.Intents.all()
    )

    self.bot_token = bot_token
    self.tree = app_commands.CommandTree(self)

  async def on_ready(self):
    print(f"{self.user.name} is ready!")

    self.tree.sync()

  def start_luna(self):
    try:
      self.run(self.bot_token)
    except discord.ClientException as err:
      print(err)