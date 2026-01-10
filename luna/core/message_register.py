from typing import Coroutine, Dict

# Class to register the message commands
class MessageCommandRegister:
  def __init__(self) -> None:
    # Dict to store the message commands(key<str> = value<Coroutine> = command_name = command_callback)
    self.commands: Dict[str, Coroutine] = {}

  # Method to store the message command 
  def register_command_message(self, name: str, callback: Coroutine) -> None:
    self.commands[name] = callback 
  
  # Method to get a message command by name
  def get_command_message(self, name: str) -> Dict[str, Coroutine]:
    return self.commands.get(name)
  
  # Method to get all message commands
  def get_all_command_messages(self) -> Dict[str, Coroutine] | None:
    return self.commands