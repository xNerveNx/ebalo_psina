import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '!' )

@client.event

async def on_ready():
    print( 'Bot Conected' )
    
@client.command()
    
async def ebalo_psina(ctx):
    for i in range(0,1000000000):
        await ctx.send('<:emoji_1:848858033786322984>')
		
		
		
		
		
		
client.run("ODQ4ODYyNDA2NjYxODk4MjUw.YLSyuA.sDaTwB9CQ7u-HA74ZpC8WJtwi-Y")