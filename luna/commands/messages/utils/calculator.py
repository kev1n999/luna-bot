import discord
from luna.core.message_handler import MessageCommandRegister

async def calculator(message: discord.Message, args):
  result = 0 

  number1 = int(args[0])
  number2 = int(args[2])
  operator = args[1]

  if operator.strip() == "+":
    result = number1 + number2 

  elif operator.strip() == "-":
    result = number1 - number2 

  elif operator.strip() == "*":
    result = number1 * number2 

  elif operator.strip() == "/":
    if number2 == 0:
      await message.reply("Erro: Divisão por 0.")
      return 
    
    result = number1 / number2   

  await message.reply(content=f"```{result}```")

def message_setup(register: MessageCommandRegister):
  register.register_command_message("calc", calculator)