from discord import *
from discord.ext import commands
import pafy
import urllib
import re
import main
import threading
import random
import asyncio
import asyncstdlib as a


class reproduction(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

#-------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def play(ctx,search):

#--------------------------------------------------------------------------------------------------------------

        def play_next():
            try:
                source=FFmpegPCMAudio(main.queue[main.i+1].getbestaudio().url,**main.FFMPEG_OPTIONS)
                ctx.voice_client.play(source,after= lambda next: play_next())
                main.i=main.i+1
            except:
                main.queue=[]
                main.i=0

#--------------------------------------------------------------------------------------------------------------

        if "https://www.youtube.com/playlist?list=" in search:
            link=urllib.request.urlopen(search)
            video_ids=re.findall(r"watch\?v=(\S{11})",link.read().decode())

            for x in video_ids:
                video=pafy.new("https://www.youtube.com/watch?v=" + x)
                video_link='https://www.youtube.com/watch?v='+video_ids[main.i]

                main.queue.append(video)
                print('')
                print(video.title)
                print(video.author)
                print(video.duration)                           #                     ||| by BetThical (`.`)
                print('')

            await ctx.send("Processing the playlist... " + "```" + search + "```")

        else:
            search='https://www.youtube.com/results?search_query='+search.replace(' ','+')
            link=urllib.request.urlopen(search)
            video_ids=re.findall(r"watch\?v=(\S{11})",link.read().decode())
            video=pafy.new('https://www.youtube.com/watch?v='+video_ids[main.i])
            video_link='https://www.youtube.com/watch?v='+video_ids[main.i]

            main.queue.append(video)
            print('')
            print(video.title)
            print(video.author)
            print(video.duration)
            print('')

            await ctx.send("Adding to the  queue " + '```' + video.title +  '```')

        if ctx.voice_client==None:
            if ctx.author.voice.channel!=None:
                await ctx.author.voice.channel.connect()
            else:
                ctx.send('You are not connected to a voice channel O.O')
        else:
            pass

        if ctx.voice_client.is_playing() == False:
            audio=main.queue[main.i].getbestaudio().url
            ctx.voice_client.play(FFmpegPCMAudio(audio,**main.FFMPEG_OPTIONS),after=lambda next: play_next())
            await ctx.send("It's playing " + '```' + video_link + ' ' + video.duration + '```')

#                    ______
#                   |      |                ──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
#                   |MY ASS|      <--       ───▄▄██▌█ beep beep ▄▄▄▌▐██▌█ "async def play"
#                   |______|            ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
#                                     ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀(@)▀

#---------------------------------------------------------------------------------------------------------------

    @commands.command()
    async def nowplaying(ctx):
        await ctx.send('Está sonando ' + '```' + str(main.queue[main.i]) + '```')

#---------------------------------------------------------------------------------------------------------------

def setup(bot):
    bot.add_command(reproduction.play)
    bot.add_command(reproduction.nowplaying)
