import os
import schedule 
import time
import discord
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

@bot.event
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)


@bot.event
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, read_messages=True)

schedule.every().day.at('16:25').do()

schedule.every().day.at('16:30').do(unlock())
bot.run(token)
while True:
    schedule.run_pending()
    time.sleep(1)
