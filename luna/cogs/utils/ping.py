from discord import app_commands, Interaction

"""Test command"""
class Ping(app_commands.Command):
  def __init__(self):
    super().__init__(
      name="ping",
      description="reply with pong",
      callback=self.callback 
    )

  async def callback(self, interaction: Interaction):
    await interaction.response.send_message("Pong!")

def setup(app: app_commands.CommandTree):
  app.add_command(Ping())