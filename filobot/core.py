import discord

from discord.ext import commands
from datetime import datetime
from utils import default

config=default.get("config.json")
start=datetime.utcnow()

client=commands.Bot(
                    command_prefix=config.prefix,
                    case_insensitive=True,
                    description=config.description,
                    owner_ids=set(config.owners)
                    )
initial_extensions=[
                    "cogs.developer",
                    "cogs.handler"
                    ]

def load_extensions(lst):
    for ext in lst:
        client.load_extension(ext)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="anime"))
    print(f"Client loaded | ID: {client.user.id}")
    
load_extensions(initial_extensions)
client.run(config.prefix)
