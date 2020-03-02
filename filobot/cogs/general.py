import discord
from discord.ext import commands
from datetime import datetime
start=datetime.utcnow() #derek fix this later kid

class GeneralCog(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command(name="info",aliases=["uptime","alive","stats"],enabled=False)
    async def info_command(self,ctx):
        elapsed=datetime.utcnow()-start #make this look nicer too sigh.
        seconds=elapsed.seconds
        seconds,minutes=divmod(seconds,60)
        minutes,hours=divmod(minutes,60)
        e=discord.Embed(title=f"ℹ️ {self.client.user.name} Statistics",description="Lists all the bot statistics currently programmed into the command.")
        e.add_field(name="Developers",value="Bot Developer ~ derek\nDashboard Developer ~ Wolfie")
        e.add_field(name="Alive",value=f"Alive and breathing for {hours}h {minutes}m {seconds}s")
        await ctx.send(embed=e)

def setup(client):
    client.add_cog(GeneralCog(client))