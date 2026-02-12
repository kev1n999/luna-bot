import discord
from discord import app_commands 
from luna.components.buttons.todolist_options import TaskOptions

class TodoListCommand(app_commands.Command):
  def __init__(self):
    super().__init__(
      name="todolist",
      description="Todolist management",
      callback=self.callback 
    )

  async def callback(self, interaction: discord.Interaction):
    view = TaskOptions()
    await interaction.response.send_message(view=view, ephemeral=True)
    
def setup(app: app_commands.CommandTree):
  app.add_command(TodoListCommand())