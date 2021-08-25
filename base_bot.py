#Imports (subject to constant change!)#

import discord
import discord.ext
from discord.ext import commands

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Establishes the bot#

bot = discord.Client()
bot = commands.Bot(command_prefix = "test:")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=("my partents fightng")))
	print("Connected and ready to talk!")
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Test command#

@bot.command()
async def ping(ctx):
    lat = str(bot.latency)[3] + str(bot.latency)[4]
    await ctx.send(f'pong! {lat}ms')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Run the bot#
#For saftey and privacy reasons we have removed the token#

bot.run("TOKEN") 
