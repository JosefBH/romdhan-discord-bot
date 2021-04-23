import time
import discord
import os
from pprint import pprint 
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
from discord.ext import commands, tasks
from prayertimes.prayertimes import PrayTimes 

load_dotenv()
token = os.getenv('TOKEN')
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

#@tasks.loop(minutes=1)
#async def checkForTime(parameter_list):
#    await return now = datetime.now()

@bot.event
async def on_ready():
    print('-------')
    print(f'we are logged in as {bot.user.name} ')
    print(f'user.id : {bot.user.id}')

@bot.command()
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)

@bot.command()
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, read_messages=True)

@bot.command()
async def start(ctx):
    while True: 
        now = datetime.now()
        now = now.strftime('%H:%M ')
        today = date.today()
        PT = PrayTimes()
        times = PT.get_times(today, (33.88, 9.53), 1)
        alimsak = times['imsak']
        almaghrib = times['maghrib']
        # pprint(times)
        pprint(now)
        # pprint(today)
        if now == almaghrib:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, read_messages=True)
            print('sahha chribtekom <3 ')
        if now == alimsak:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            print('rabi yet9abbel')





bot.run(token)
