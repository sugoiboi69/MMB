import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio




bot = commands.Bot(command_prefix='#')
print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.send_message(general, ":ping_pong: ping!! xSSS")
    print ("user has pinged")   

bot.run('mmsgb69@gmail.com', 'succgod123') 

