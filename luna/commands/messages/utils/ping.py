import discord 
from luna.core.message_register import MessageCommandRegister
from luna.services.google_genai import send_prompt

async def luna_callback(message: discord.Message, *args):
  response = send_prompt(args)

  if not response:
    await message.reply("Ocorreu um erro")

  await message.channel.send(response)

def message_setup(register: MessageCommandRegister):
  register.register_command_message("hi", luna_callback)