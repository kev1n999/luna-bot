import discord 
from discord import app_commands 
from luna.core.message_register import MessageCommandRegister

# Main class of LunaBot to connect the discord client
class LunaClient(discord.Client):
  def __init__(self, bot_token: str, command_prefix: str, message_commands: MessageCommandRegister) -> None:
    super().__init__(
      intents=discord.Intents.all()
    )
    
    self.bot_token = bot_token
    self.tree = app_commands.CommandTree(self)
    self.command_prefix = command_prefix
    self.message_commands = message_commands

  async def on_ready(self) -> None:
    print(f"{self.user.name} is ready!")
    all_commands = self.message_commands.get_all_command_messages()

    if all_commands:
      print(f"Message Commands:\n{[k for k, _ in all_commands.items()]}")
    
    await self.tree.sync()
  
  async def on_message(self, message: discord.Message):
    if message.author.bot:
      return 
    
    if not message.content.startswith(self.command_prefix):
      return 
    
    message_content = message.content[len(self.command_prefix):].strip().lower()
    if not message_content:
      return 
    
    name, *args = message_content.split()
    message_command = self.message_commands.get_command_message(name)

    if message_command:
      await message_command(message, args)

  # Functions to start the luna bot
  def start_luna(self) -> None:
    try:
      self.run(self.bot_token)
    except discord.ClientException as err:
      print(err)