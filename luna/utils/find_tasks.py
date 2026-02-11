import os 
import json 
import discord 

def format_json(string: str) -> str:
  return string.replace("'", '"').replace("ObjectId", "").replace("(", "").replace(")", "")

async def find_tasks(interaction: discord.Interaction, founded_tasks: list | dict):
  parse = format_json(str([tasks for tasks in founded_tasks]))

  json_serialize = json.loads(format_json(str(founded_tasks)) if not isinstance(founded_tasks, list) else parse)
  with open("tasks.json", "w", encoding="utf-8") as tasks_json_file:
    json.dump(json_serialize, tasks_json_file, indent=2, ensure_ascii=False)

  await interaction.response.send_message(file=discord.File(fp="tasks.json"), ephemeral=True)
  os.remove("tasks.json")