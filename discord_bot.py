import os
import discord
from dotenv import load_dotenv
import re
import json

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
    tags = {}
    async for message in channel.history(limit = 25*44):
        tag = re.findall(pattern, message.content)
        author = message.author.name
        if tag:
            tags[tag[0]] = author
    #tags = flatten(tags)
    tags['gallon'] = 'gallon'
    tags['jambre'] = 'jambre'
    with open("./json/tags.json", "w") as f:
        json.dump(tags, f)

    print("done")

client.run(TOKEN)

