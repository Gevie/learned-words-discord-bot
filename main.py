"""The main file"""

import os
import discord
from discord.ext import commands
from discord import Intents  # Import Intents class
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


bot.load_extension('src.bot.command')
bot.run(DISCORD_TOKEN)
