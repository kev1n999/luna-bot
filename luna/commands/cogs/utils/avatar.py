import discord 
from discord.ui import View, UserSelect
from discord import app_commands 

class AvatarCommand(app_commands.Command):
  def __init__(self):
    super().__init__(
      name="avatar",
      description="Returns the avatar by mentioned user",
      callback=self.callback 
    )

  async def callback(self, interaction: discord.Interaction, user: discord.User=None):
    if user is None:
      user = interaction.user 

    user_avatar = user.display_avatar

    embed = discord.Embed(
      title=f"Avatar de {user.name}",
      color=discord.Colour.magenta()
    ) 

    embed.set_image(url=user_avatar)

    user_select = UserSelect(placeholder="Selecionar outro usuário...")
    view = View()
    view.add_item(user_select)

    await interaction.response.send_message(embed=embed, view=view)

def setup(app: app_commands.CommandTree):
  app.add_command(AvatarCommand())