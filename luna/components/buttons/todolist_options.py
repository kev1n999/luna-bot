import discord
from discord import ui 
from discord import ButtonStyle
from luna.components.modals.todolist_fields import TaskFields

class TaskOptions(ui.LayoutView):
  row = ui.ActionRow()

  @row.button(label="Create", style=ButtonStyle.green)
  async def create_task(self, interaction: discord.Interaction, button: ui.BUtton):
    modal = TaskFields()
    await interaction.response.send_modal(modal)

  @row.button(label="Vself, interaction: discord.Interactioniew", style=ButtonStyle.secondary)
  async def view_task(self, interaction: discord.Interaction, button: ui.BUtton):
    pass 

  @row.button(label="Update", style=ButtonStyle.gray)
  async def update_task(self, interaction: discord.Interaction, button: ui.BUtton):
    pass 

  @row.button(label="Delete", style=ButtonStyle.red)
  async def delete_task(self, interaction: discord.Interaction, button: ui.BUtton):
    pass