from discord import *
from discord.ext import commands
import os
import asyncio

#-------------------------------some useful constants they'll be used later -------------------------------------------

i=0
queue=[]
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

#----------------------------------------------------------------------------------------------------------------------

bot=commands.Bot(command_prefix='-')

#----------------------------------------------------------------------------------------------------------------------

@bot.event  # Ready ones say brrrrrrrrrrrrrrrrrrrrr
async def on_ready():
    await bot.change_presence(status=Status.dnd, activity=Game('Cocinar filete'))
    print('Succesfuly started')

#----------------------------------------------------------------------------------------------------------------------

def runner():
    bot.run('ODgxNTg5NzkwNDYwNDg5Nzk4.YSvCeQ.6ScqV33qpXtS4qnXhizPOMf7H3Y') 

#-----------------------------------------------loading other files----------------------------------------------------

bot.utils = [
    "utils.voice",
    "utils.controls",
    "utils.misc",
]

for util in bot.utils:
    bot.load_extension(util)

#-------------------------------running the bot when executing this program file---------------------------------------

if __name__=='__main__':
    runner()  # makes the bot to run UwU

