import discord
from luna.core.message_handler import MessageCommandRegister

async def calculator(message: discord.Message, args):
  result = 0 
  operator = None 
  
  try:
    number1 = int(args[0])
    number2 = int(args[2])
    operator = args[1]
  except Exception:
    if isinstance(Exception, IndexError):
      await message.reply("Erro: argumentos inválidos", delete_after=10.0)
  
  if not operator:
    await message.reply("Erro: Você precisa informar um operator como: `+, -, /, *`")

  if operator.strip() == "+":
    result = number1 + number2 

  elif operator.strip() == "-":
    result = number1 - number2 

  elif operator.strip() == "*" or operator.strip() == "x":
    result = number1 * number2 

  elif operator.strip() == "/":
    if number2 == 0:
      await message.reply("Erro: Divisão por 0.", delete_after=10.0)
      return 
    
    result = number1 / number2   

  await message.reply(content=f"```{result}```")

def message_setup(register: MessageCommandRegister):
  register.register_command_message("calc", calculator)