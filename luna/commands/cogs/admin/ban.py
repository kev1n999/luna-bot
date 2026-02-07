import discord
from discord import app_commands, DiscordException
from luna.config.constants import DEFAULT_EMBED_COLOR

class BanCommand(app_commands.Command):
  def __init__(self):
    super().__init__(
      name="ban",
      description="ban the mentioned member [only adm]",
      callback=self.callback
    )

  async def callback(self, interaction: discord.Interaction, member: discord.Member, reason: str=None):
    if not interaction.user.guild_permissions.administrator:
      return await interaction.response.send_message(
        content="You're not allowed to use this command!",
        ephemeral=True 
      )
    
    if len(member.guild_permissions) >= interaction.user:
      return await interaction.response.send_message(
        content="The mentioned user has the same permissions as you!",
        ephemeral=True 
      )
    
    try:
      await member.ban(reason=reason) 
      embed = discord.Embed(
        title="Banned user",
        description=None if not reason else f"`{reason}`",
        color=DEFAULT_EMBED_COLOR
      )

      embed.set_thumbnail(url=member.display_avatar.url)
      await interaction.channel.send(embed=embed)
    except DiscordException as err:
      await interaction.response.send_message(
        content="An error ocurred to ban that user, try again!",
        ephemeral=True
      )
      print(f"an error ocurred to ban that user\n {err}")
    
def setup(app: app_commands.CommandTree):
  app.add_command(BanCommand())
