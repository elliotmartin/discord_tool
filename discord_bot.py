import os
import discord
from dotenv import load_dotenv
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

pattern = r"[a-zA-Z0-9]+#[0-9]+"

client = discord.Client()

flatten = lambda l: [item for sublist in l for item in sublist]

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    channel = discord.utils.find(lambda c: c.name == "battletags", guild.channels)
    print(channel)
    tags = []
    async for message in channel.history(limit = 25*34):
        tag = re.findall(pattern, message.content)
        tags.append(tag)
    tags = flatten(tags)
    with open("tags.txt", "w") as f:
        for t in tags:
            f.write(t + "\n")
    print("done")

client.run(TOKEN)

