"""The main file for the leanred words bot module"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)

bot = commands.Bot(command_prefix="!", description='A bot for managing learned words (language learning)')
bot.load_extension('commands')


@bot.event
async def on_ready():
    """
    Runs on bot on ready event

    Returns:
        None
    """

    game = discord.Game("StephenGV is currently programming, testing and debugging me.")
    await bot.change_presence(status=discord.Status.idle, activity=game)


load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'), bot=True, reconnect=True)
