# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
"""TOKEN = os.getenv('DISCORD_TOKEN')"""
TOKEN = 'MTA5MjQ4OTA1NDY1NTg3NzEyMQ.GlGSgX.I6GzTM2GDCk_bHaq-h4I2Soc-3A9OhpeyBXHIE'


client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    GUILD = client.guilds[0]
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    nel = discord.utils.get(guild.members, name="Nebu")

    print (nel)
    discord.utils.

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)