from typing import Coroutine, Dict

class MessageCommandRegister:
  def __init__(self):
    self.commands: Dict[str, Coroutine] = {}

  def register_command_message(self, name: str, callback: Coroutine) -> None:
    self.commands[name] = callback 
  
  def get_command_message(self, name: str) -> Dict[str, Coroutine]:
    return self.commands.get(name)

  def get_all_command_messages(self) -> Dict[str, Coroutine] | None:
    return self.commands