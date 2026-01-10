import os 
import importlib.util
from discord.app_commands import CommandTree

def load_cogs(root_dir: str, app: CommandTree):
  # The directory to cogs folder
  cogs_folder = os.path.join(root_dir, "cogs")

  # Acess the caregorys(sub-folders) into cogs folder(main folder)
  for categorys in os.listdir(cogs_folder):
    if "__init__" in categorys:
      continue 

    for files in os.listdir(f"{cogs_folder}/{categorys}"):
      if not files.endswith(".py") or files.startswith("__init__"):
        continue 
      
      try:
        module_name = f"cogs.{categorys}.{files[:-3]}"
        module_path = os.path.join(cogs_folder, categorys, files)

        spec = importlib.util.spec_from_file_location(module_name, module_path)

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "setup"):
          module.setup(app)
        
        print("Loaded commands:\n")
        print(files[:-3], end="\n")
      except Exception as err:
        print(err)