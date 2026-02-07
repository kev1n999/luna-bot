import discord 
from discord import ui, TextStyle
from luna.database.queries.todolist import Task

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
    task = Task(
      name=self.task_name.value,
      description=self.task_description.value, 
    )

    created_task = task.create_task(interaction.user.id)

    if not created_task:
      return await interaction.response.send_message(
        content="Ocorreu um erro ao criar a task!",
        ephemeral=True, 
      )
    
    await interaction.response.send_message(content="Task criada com sucesso!", ephemeral=True)