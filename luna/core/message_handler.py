import os
import importlib.util  
from .message_register import MessageCommandRegister

def load_messages(root_dir: str, register: MessageCommandRegister) -> None:
  # The directoty of the message-commands path 
  messages_folder = os.path.join(root_dir, "commands", "messages")

  # Acess the caregorys(sub-folders) into message-commands folder(main folder)
  for categorys in os.listdir(messages_folder):
    # Ignores the __init__.py file in the categorys folder
    if "__init__" in categorys:
      continue 

    # Acess the files in the categorys folder
    for files in os.listdir(f"{messages_folder}/{categorys}"):
      # Ignore files that are not .py and __init__.py
      if not files.endswith(".py") or files.startswith("__init__"):
        continue 

      try:
        # Found the message-command modules 
        module_name = f"commands.messages.{categorys}.{files[:-3]}"
        module_path = os.path.join(messages_folder, categorys, files)

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "message_setup"):
          # Execute the function to register the message-command
          module.message_setup(register)
      except Exception as err:
        print(err)