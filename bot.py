import os 
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
@bot.command()
async def on_asha(ctx):
    while True:
        now = datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:00')
        print(now)
        if asha == now:
            await ctx.send('@D3adshot#0587 ')    



@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

@bot.command()
async def s(ctx):
    print(ctx.guild.default_role) 
@bot.command()
async def add(ctx, left: float, right: float):
    """Adds two numbers together."""""
    await ctx.send(left + right)

@bot.command()
async def saymin(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
        

@bot.command()
async def ftarna(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True,read_messages=True)

bot.run(token)
'''
@client.event
async def isReady():
    for guild in client.guilds: 
        print(guild)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('hello man !')
        print(message.author, message.content)

@client.command()
async def perm(ctx):
    print(ctx) 
    await ctx.channel.set_permissions(send_messages=False)
    
client.run(token)
'''
