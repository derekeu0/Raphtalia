import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self,client):
        self.client=client
        self.errorchannel=client.get_channel(662486430580211752)

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if hasattr(ctx.command,"on_error"):
            return
        
        ignored=()

        if isinstance(error,ignored):
            return
        elif isinstance(error,commands.CommandNotFound):
            await ctx.message.add_reaction("🤷‍♂️")
        elif isinstance(error,commands.NotOwner):
            await ctx.message.add_reaction("⛔")
        else:
            e=discord.Embed(title="⚠️ Unknown Error",description=f"There was an unregistered error. The developers have been contacted.",color=0xff0000)
            e.add_field(name="Error",value=f"```py\n{error}```")
            await ctx.send(embed=e)
            e.add_field(name="Location",value=f"[Jump To Error]({ctx.message.jump_url})",inline=False)
            await self.errorchannel.send("<@&664992967437844481>")
            await self.errorchannel.send(embed=e)

def setup(client):
    client.add_cog(CommandErrorHandler(client))