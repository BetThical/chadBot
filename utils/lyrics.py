from discord import *
from discord.ext import commands
import urllib
from main import *
import reproduction

class lyrics(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()


def setup(bot):
    bot.add_command(lyrics.lyrics)

