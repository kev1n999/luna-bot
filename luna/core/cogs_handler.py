import os 
import importlib.util
from discord.app_commands import CommandTree

# Function to load command cogs(Slash Commands)
def load_cogs(root_dir: str, app: CommandTree) -> None:
  # The directory of the cogs path
  cogs_folder = os.path.join(root_dir, "commands", "cogs")

  # Acess the caregorys(sub-folders) into cogs folder(main folder)
  for categorys in os.listdir(cogs_folder):
    # Ignores the __init__.py file in the categorys folder
    if "__init__" in categorys:
      continue 

    # Acess the files in the categorys folder
    for files in os.listdir(f"{cogs_folder}/{categorys}"):
      # Ignore files that are not .py and __init__.py
      if not files.endswith(".py") or files.startswith("__init__"):
        continue 
      
      try:
        # Found the cogs modules 
        module_name = f"commands.cogs.{categorys}.{files[:-3]}"
        module_path = os.path.join(cogs_folder, categorys, files)

        spec = importlib.util.spec_from_file_location(module_name, module_path)

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "setup"):
          # Execute the function to add a new command to the CommandTree 
          module.setup(app)
      except Exception as err:
        print(err)