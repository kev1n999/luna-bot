import os
import importlib.util  
from luna.config.message_command import MessageCommandRegister

def load_messages(root_dir: str, register: MessageCommandRegister) -> None:
  messages_folder = os.path.join(root_dir, "messages")

  for categorys in os.listdir(messages_folder):
    if "__init__" in categorys:
      continue 

    for files in os.listdir(f"{messages_folder}/{categorys}"):
      if not files.endswith(".py") or files.startswith("__init__"):
        continue 

      try:
        module_name = f"messages.{categorys}.{files[:-3]}"
        module_path = os.path.join(messages_folder, categorys, files)

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "message_setup"):
          module.message_setup(register)
      except Exception as err:
        print(err)