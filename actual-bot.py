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

@bot.event
async def speak():
    speech = input('Speak: ')
    await bot.say(speech)

@bot.event
while True:
    await speak()


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.send_message(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def oof(ctx):
    while True:
        time.sleep(1)
        await bot.say("->game pokemon")  
        await bot.say("end")

@bot.command(pass_context=True)
async def pokemonspam(ctx):
    while True:
        await bot.say('->game pokemon')
        async def on_message(message):
            dict_of_attachments = message.attachments[0]
            google_images_link = "https://www.google.com/searchbyimage?&image_url=" + str(dict_of_attachments['url'])
            print(google_images_link)
        await bot.say('end')
        time.sleep(5)

@bot.command(pass_context=True)
async def startloot(ctx):
    while True:
        await bot.say('->loot')
        time.sleep(300)

@bot.command(pass_context=True)
async def xfer(ctx):
    await bot.say('->transfer @borgr#1821 all')


        



    
    


bot.run('mmsgb69@gmail.com', 'succgod123')

