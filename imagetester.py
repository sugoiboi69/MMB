#dependencies (don't delete retard)
import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys 

bot = commands.Bot(command_prefix='#')
print ("---------------------------------------------------")
print ("RUNNING ON DISCORD VERSION: " + discord.__version__)
print ("---------------------------------------------------")

@bot.event
async def 

@bot.event
#initiation console message
async def on_ready():
    print ("███████████████████████ hishi's FAT mantaro moolahmaker ███████████████████████")
    print ("███████████████████████████ running on account: " + bot.user.name + " ████████████████████████████")
    print ("███████████████████████████ with ID: " + bot.user.id + " ███████████████████████████")
    print ("███████████████████████████ licensed by: ur mom LUL ███████████████████████████████")
    time.sleep(1)
    print ("--------------------------- BEGINNING OF CHAT LOG ---------------------------------")

#log each message, searches images posted    

@bot.event


@bot.event
async def on_message(message):

    if len(message.embeds)>0:
        print(str(message.author)+": | Embed Attached")
        print("----")
        embed_list = message.embeds[0]
        embed_image = embed_list['image']
        image_url = embed_image['url']
        google_images_link = "https://www.google.com/searchbyimage?&image_url=" + str(image_url)
        driver = webdriver.Firefox()
        driver.get(google_images_link)
        divs = driver.find_element_by_class_name("r5a77d")
        bestguess = divs.find_element_by_class_name("fKDtNb").text
        list_of_results = driver.find_elements_by_class_name('r')
        await bot.send_message(message.channel, 'The image seems to be: ' + str(bestguess))
        await bot.send_message(message.channel, '----------------------------------------------------------------')
        await bot.send_message(message.channel,'Here are search results for the image:')
        async def msgresults():
            for x in list_of_results:
                result = x.text
                await bot.send_message(message.channel, result)
                await bot.send_message(message.channel, '---------------------------------------------------------')
        await msgresults()
        driver.close()

    elif len(message.attachments)>0:
        print(str(message.author) + ': ' + str(message.content) + " | Image Attached")
        print("----")
        dict_of_attachments = message.attachments[0]
        google_images_link = "https://www.google.com/searchbyimage?&image_url=" + str(dict_of_attachments['url'])
        driver = webdriver.Firefox()
        driver.get(google_images_link)
        divs = driver.find_element_by_class_name("r5a77d")
        bestguess = divs.find_element_by_class_name("fKDtNb").text
        print('-----------------------------------------------------')
        await bot.send_message(message.channel, 'The image seems to be: ' + str(bestguess))
        driver.close()

    elif len(message.content)>0:
        print(str(message.author) + ': ' + str(message.content))
        if 'correctly!' in str(message.content):
            await sys.exit(msgresults())
        elif 'end' in str(message.content):
            await sys.exit(msgresults())
        

        
        
#logs into the bot account (don't ban me plz lul)
bot.run('mmsgb69@gmail.com', 'succgod123')