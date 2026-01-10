import discord 
from luna.core.message_register import MessageCommandRegister

async def ping_callback(message: discord.Message, *args):
  await message.channel.send("Hi! I'm luna and i like bananas")

def message_setup(register: MessageCommandRegister):
  register.register_command_message("hi", ping_callback)