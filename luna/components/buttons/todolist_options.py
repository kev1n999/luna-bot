import discord
from discord import ui 
from discord import ButtonStyle
from luna.components.modals.todolist_fields import TaskFields, DeleteTaskById
from luna.database.queries.todolist import Task

class DeleteTaskButtons(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="By id", style=ButtonStyle.primary)
  async def delete_task_by_id(self, interaction: discord.Interaction, button: ui.Button):
    modal = DeleteTaskById()
    await interaction.response.send_modal(modal)

  @row.button(label="Delete all", style=ButtonStyle.red)
  async def delete_task(self, interaction: discord.Interaction, button: ui.Button):
    task = Task()
    try:
      task.delete_task(user_id=interaction.user.id)
      await interaction.response.send_message(content="Todas as suas tasks foram deletadas!", ephemeral=True)
    except Exception as err:
      print(f"An error ocurred to delete all tasks\n {err}")
      await interaction.response.send_message(content="Ocorreu um erro ao deletar todas as suas tasks!", ephemeral=True)

class TaskOptions(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="Create", style=ButtonStyle.green)
  async def create_task(self, interaction: discord.Interaction, button: ui.Button):
    modal = TaskFields()
    await interaction.response.send_modal(modal)

  @row.button(label="Get tasks", style=ButtonStyle.primary)
  async def view_task(self, interaction: discord.Interaction, button: ui.Button):
    ...

  @row.button(label="Update", style=ButtonStyle.gray)
  async def update_task(self, interaction: discord.Interaction, button: ui.Button):
    ... 

  @row.button(label="Delete", style=ButtonStyle.red)
  async def delete_task(self, interaction: discord.Interaction, button: ui.Button):
    view = DeleteTaskButtons()
    await interaction.response.send_message(view=view)