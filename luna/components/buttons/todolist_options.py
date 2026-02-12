import discord
from discord import ui 
from discord import ButtonStyle
from luna.components.modals.todolist_fields import TaskFields, DeleteTaskById, FindTaskById
from luna.database.queries.todolist import Task
from luna.core.errors_handler import TaskNotExists
from luna.utils.find_tasks import find_tasks

class TaskStatusOptions(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="CREATED", style=ButtonStyle.green)
  async def created_status(self, interaction: discord.Interaction, _):
    pass 

  @row.button(label="PENDING", style=ButtonStyle.secondary)
  async def pending_status(self, interaction: discord.Interaction, _):
    pass 

  @row.button(label="COMPLETED", style=ButtonStyle.red)
  async def completed_status(self, interaction: discord.Interaction, _):
    pass 
  
  @row.button(label="Back", style=ButtonStyle.secondary)
  async def back_options(self, interaction: discord.Interaction, _):
    view = TaskOptions()
    await interaction.response.edit_message(view=view)

class UpdateTaskButtons(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="Name", style=ButtonStyle.green)
  async def change_task_name(self, interaction: discord.Interaction, _):
    view = TaskStatusOptions()
    await interaction.response.edit_message(view=view)

  @row.button(label="Description", style=ButtonStyle.gray)
  async def change_task_description(self, interaction: discord.Interaction, _):
    view = TaskStatusOptions()
    await interaction.response.edit_message(view=view)

  @row.button(label="Status", style=ButtonStyle.blurple)
  async def change_task_status(self, interaction: discord.Interaction, _):
    view = TaskStatusOptions()
    await interaction.response.edit_message(view=view)

  @row.button(label="Back", style=ButtonStyle.secondary)
  async def back_options(self, interaction: discord.Interaction, _):
    view = TaskOptions()
    await interaction.response.edit_message(view=view)

class DeleteTaskButtons(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="By id", style=ButtonStyle.primary)
  async def delete_task_by_id(self, interaction: discord.Interaction, _):
    modal = DeleteTaskById()
    await interaction.response.send_modal(modal)

  @row.button(label="Delete all", style=ButtonStyle.red)
  async def delete_task(self, interaction: discord.Interaction, _):
    task = Task()
    try:
      task.delete_task(user_id=interaction.user.id)
      await interaction.response.send_message(content="Todas as suas tasks foram deletadas!", ephemeral=True)
    except Exception as err:
      print(f"An error ocurred to delete all tasks\n {err}")
      await interaction.response.send_message(content="Ocorreu um erro ao deletar todas as suas tasks!", ephemeral=True)

class FindTasksButton(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="By id", style=ButtonStyle.green)
  async def find_by_id(self, interaction: discord.Interaction, _):
    modal = FindTaskById()
    await interaction.response.send_modal(modal)

  @row.button(label="Find all", style=ButtonStyle.red)
  async def find_all(self, interaction: discord.Interaction, _):
    task = Task()

    try:
      founded_tasks = task.find_tasks(user_id=interaction.user.id) 
      await find_tasks(interaction, founded_tasks)
    except Exception as err:
      if isinstance(err, TaskNotExists):
        await interaction.response.send_message(content="Tasks not found!", ephemeral=True)
      else: 
        await interaction.response.send_message(content="An error ocurred to fetch tasks!", ephemeral=True)
      print(err)
  
  @row.button(label="Back", style=ButtonStyle.secondary)
  async def back_options(self, interaction: discord.Interaction, _):
    view = TaskOptions()
    await interaction.response.edit_message(view=view)

class TaskOptions(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="Create", style=ButtonStyle.green)
  async def create_task(self, interaction: discord.Interaction, _):
    modal = TaskFields()
    await interaction.response.send_modal(modal)

  @row.button(label="Get tasks", style=ButtonStyle.primary)
  async def view_task(self, interaction: discord.Interaction, _):
    view = FindTasksButton()
    await interaction.response.edit_message(view=view)

  @row.button(label="Update", style=ButtonStyle.gray)
  async def update_task(self, interaction: discord.Interaction, _):
    view = UpdateTaskButtons()
    await interaction.response.edit_message(view=view)

  @row.button(label="Delete", style=ButtonStyle.red)
  async def delete_task(self, interaction: discord.Interaction, _):
    view = DeleteTaskButtons()
    await interaction.response.edit_message(view=view)

  @row.button(label="Back", style=ButtonStyle.secondary)
  async def back_options(self, interaction: discord.Interaction, _):
    view = TaskOptions()
    await interaction.response.edit_message(view=view)