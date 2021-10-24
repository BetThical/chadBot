import discord                              
import random
import main
from discord.ext import commands

class musicControls(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

#----------------------------------------------------------------------------------------------------------    

    @commands.command()
    async def disconnect(ctx):
        if ctx.author.voice.channel!=None:
            print('The queue has been succesfully cleaned')
            await ctx.voice_client.disconnect()
            main.queue=[]
        else:
            await ctx.send('El bot no se encuentra en ningun canal de voz')

#----------------------------------------------------------------------------------------------------------

    @commands.command()
    async def stop(ctx):
        if ctx.voice_client.is_playing() == True:
            ctx.voice_client.stop()
            main.queue=[]
            main.i=0
            await ctx.send('Stopeando la musica')

#----------------------------------------------------------------------------------------------------------

    @commands.command()
    async def skip(ctx):                            
        if ctx.voice_client.is_playing() == True:    #                     ||| by BetThical (`.`)


            ctx.voice_client.stop()
            await ctx.send('Skipeando la cancion')

#----------------------------------------------------------------------------------------------------------

    @commands.command()
    async def shuffle(ctx):
        random.shuffle(main.queue)
        main.i=-1
       
        print("a")
        print(main.queue)

        if ctx.voice_client.is_playing() == True:
            random.shuffle(main.queue)
            main.i=-1
       
            print("a")
            print(main.queue)
            ctx.voice_client.stop()
            
            print("\n b")

#----------------------------------------------------------------------------------------------------------

def setup(bot):
    bot.add_command(musicControls.disconnect)
    bot.add_command(musicControls.stop)
    bot.add_command(musicControls.skip)
    bot.add_command(musicControls.shuffle)


