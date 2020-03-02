import discord
from discord.ext import commands

class DeveloperCog(commands.Cog,command_attrs=dict(hidden=True)):
    def __init__(self,client):
        self.client=client

    @commands.group(name="ext",invoke_without_command=True)
    @commands.is_owner()
    async def ext_base(self,ctx):
        e=discord.Embed(title="⚙️ Loaded Extensions",description="Shows all the extensions that have been loaded.",color=0xff0000)
        e.add_field(name="Loaded Extensions",value=",\n".join([ext.replace("cogs.","") for ext in self.client.extensions])) #derek look at this later and make it better
        await ctx.send(embed=e)

    @ext_base.command(name="load")
    @commands.is_owner()
    async def ext_load(self,ctx,*,ext):
        try:
            self.client.load_extension(f"cogs.{ext.lower()}")
        except AttributeError as error:
            e=discord.Embed(title="⚠️ Attribute Error",description=f"There was an attribute error.",color=0xff0000)
            e.add_field(name="Error",value=f"```py\n{error}```")
            await ctx.message.add_reaction("❌")
            return await ctx.send(embed=e)
        except commands.ExtensionError as error:
            e=discord.Embed(title="⚠️ Extension Error",description=f"There was an extension error.",color=0xff0000)
            e.add_field(name="Error",value=f"```py\n{error}```")
            await ctx.message.add_reaction("❌")
            return await ctx.send(embed=e)
        await ctx.message.add_reaction("👍")
    
    @ext_base.command(name="unload")
    @commands.is_owner()
    async def ext_unload(self,ctx,*,ext):
        if ext.lower()=="developer":
            await ctx.send("You **REALLY** don't wanna do that.")
        else:
            try:
                self.client.unload_extension(f"cogs.{ext.lower()}")
            except AttributeError as error:
                e=discord.Embed(title="⚠️ Attribute Error",description=f"There was an attribute error.",color=0xff0000)
                e.add_field(name="Error",value=f"```py\n{error}```")
                await ctx.message.add_reaction("❌")
                return await ctx.send(embed=e)
            except commands.ExtensionError as error:
                e=discord.Embed(title="⚠️ Extension Error",description=f"There was an extension error.",color=0xff0000)
                e.add_field(name="Error",value=f"```py\n{error}```")
                await ctx.message.add_reaction("❌")
                return await ctx.send(embed=e)
            await ctx.message.add_reaction("👍")
    
    @ext_base.command(name="reload")
    @commands.is_owner()
    async def ext_reload(self,ctx,*,ext):
        try:
            if ext.lower() == "all":
                for ext in self.client.extensions:
                    self.client.reload_extension(ext)
            else:
                self.client.reload_extension(f"cogs.{ext.lower()}")
        except AttributeError as error:
            e=discord.Embed(title="⚠️ Attribute Error",description=f"There was an attribute error.",color=0xff0000)
            e.add_field(name="Error",value=f"```py\n{error}```")
            await ctx.message.add_reaction("❌")
            return await ctx.send(embed=e)
        except commands.ExtensionError as error:
            e=discord.Embed(title="⚠️ Extension Error",description=f"There was an extension error.",color=0xff0000)
            e.add_field(name="Error",value=f"```py\n{error}```")
            await ctx.message.add_reaction("❌")
            return await ctx.send(embed=e)
        await ctx.message.add_reaction("👍")

def setup(client):
    client.add_cog(DeveloperCog(client))