import discord 
from luna.core.message_register import MessageCommandRegister

async def ping_command(message: discord.Message, args):
  await message.reply("Pong!")

def message_setup(register: MessageCommandRegister):
  register.register_command_message("ping", ping_command)