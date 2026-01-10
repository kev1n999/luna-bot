import discord 
from luna.core.message_register import MessageCommandRegister

async def ping_callback(message: discord.Message, *args):
  await message.channel.send("Pong!")

def message_setup(register: MessageCommandRegister):
  register.register_command_message("ping", ping_callback)