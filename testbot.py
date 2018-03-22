#bot lul

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix= '=')

@bot.event

#print to console when logged in
async def on_ready():
    print('ur shit ready fam')
    print('my name is: ' + bot.user.name)
    print('my ID is: ' + bot.user.id)

@bot.command(pass_context = True)
async def ping(ctx):
    await bot.say(':ping_pong: pong bitch :ping_pong:')

@bot.command(pass_context = True)
async def info(ctx, user: discord.Member):
    await bot.say('ur username is {}'.format(user.name))        

bot.run('mmsgb69@gmail.com', 'succgod123')    