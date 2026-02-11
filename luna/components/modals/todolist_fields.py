import discord 
from discord import ui, TextStyle
from luna.database.queries.todolist import Task
from luna.utils.find_tasks import find_tasks

class FindTaskById(ui.Modal):
  def __init__(self):
    super().__init__(
      title="Find task by id",
    )
    
  task_id = ui.TextInput(
    label="Task ID",
    placeholder="Type the task id here",
    required=True,
    style=TextStyle.short,
  )

  async def on_submit(self, interaction: discord.Interaction):
    task = Task()

    try:
      founded_tasks = task.find_tasks(id=self.task_id.value) 
      await find_tasks(interaction, founded_tasks)
    except Exception as err:
      print(f"An error ocurred to fetch tasks!\n{err}")
      await interaction.response.send_message(content="an error ocurred to fetch tasks!!", ephemeral=True)

class DeleteTaskById(ui.Modal):
  def __init__(self):
    super().__init__(
      title="Delete task by id"
    )

  task_id = ui.TextInput(
    label="Task ID",
    placeholder="Type the task id here",
    required=True,
    style=TextStyle.short,
  )

  async def on_submit(self, interaction: discord.Interaction):
    task = Task()

    try:
      task.delete_task(self.task_id.value)
      await interaction.response.send_message(content="Task deleted!", ephemeral=True)
    except Exception as err:
      print(f"An error ocurred to delete the task\n{err}")
      await interaction.response.send_message(content="an error ocurred to delete the task!", ephemeral=True)

class TaskFields(ui.Modal):
  def __init__(self):
    super().__init__(
      title="Create a new task",
    )

  task_name = ui.TextInput(
    label="Task name",
    placeholder="Type the task name",
    required=True,
    style=TextStyle.short, 
  )
  task_description = ui.TextInput(
    label="Task description",
    placeholder="Type the task description",
    required=True,
    style=TextStyle.paragraph, 
  )

  async def on_submit(self, interaction: discord.Interaction):
    task = Task()

    try:
      task.create_task(self.task_name.value, self.task_description.value, user_id=interaction.user.id)
      await interaction.response.send_message(content="Task created!", ephemeral=True)
    except Exception as err:
      print(f"An error ocurred to create the task\n{err}")
      await interaction.response.send_message(
        content="an error ocurred to create the task!",
        ephemeral=True, 
      )