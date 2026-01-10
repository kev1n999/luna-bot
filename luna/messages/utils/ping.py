import discord 
from luna.config.message_command import MessageCommandRegister

async def ping_callback(message: discord.Message, *args):
  await message.channel.send("Pong!")

def message_setup(register: MessageCommandRegister):
  register.register_command_message("ping", ping_callback)
  print(register.get_all_command_messages())