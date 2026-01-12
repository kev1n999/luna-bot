import discord 
from luna.core.message_handler import MessageCommandRegister
from luna.services.google_genai import send_prompt

async def agent_message(message: discord.Message, args):
  if not args:
    args = "olá!"
    
  response = send_prompt(args)
  await message.reply(content=response)
  
def message_setup(register: MessageCommandRegister):
  register.register_command_message("luna", agent_message)
