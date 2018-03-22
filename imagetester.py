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

bot = commands.Bot(command_prefix='#')
print ("RUNNING ON DISCORD VERSION: " + discord.__version__)

@bot.event
#initiation console message
async def on_ready():
    print ("███████████████████████ hishi's FAT mantaro moolahmaker ███████████████████████")
    print (" ")
    print ("███████████████████████████ running on account: " + bot.user.name + " ████████████████████████████")
    print (" ")
    print ("███████████████████████████ with ID: " + bot.user.id + " ███████████████████████████")
    print (" ")
    print ("███████████████████████████ licensed by: ur mom LUL ███████████████████████████████")
    print (" ")
    print ("--------------------------- BEGINNING OF CHAT LOG ---------------------------------")
    print (" ")
    print (" ")

@bot.event
async def on_message(message):
    if len(message.content)>0:
        print(str(message.author) + ': ' + str(message.content))

    elif len(message.embeds[0])>0:
        embed_list = message.embeds[0]
        embed_image = embed_list['image']
        image_url = embed_image['url']
        google_images_link = "https://www.google.com/searchbyimage?&image_url=" + str(image_url)
        drvpath = "D:\Documents\pythy discbot"
        driver = webdriver.Firefox(drvpath)
        driver.get(google_images_link)
        divs = driver.find_element_by_class_name("r5a77d")
        bestguess = divs.find_element_by_class_name("fKDtNb").text
        list_of_results = str(driver.find_elements_by_link_text('Pokemon'))
        await bot.send_message(message.channel, 'The image seems to be: ' + str(bestguess))
        await bot.send_message(message.channel, '----------------------------------------------------------------')
        print(len(list_of_results))
        

        driver.close()    

    else:
        print(str(message.author) + ': ' + str(message.content) + " | " + "--Image Attached--")
        dict_of_attachments = message.attachments[0]
        google_images_link = "https://www.google.com/searchbyimage?&image_url=" + str(dict_of_attachments['url'])
        drvpath = "D:\Documents\pythy discbot"
        driver = webdriver.Firefox(drvpath)
        driver.get(google_images_link)
        divs = driver.find_element_by_class_name("r5a77d")
        bestguess = divs.find_element_by_class_name("fKDtNb").text
        print('-----------------------------------------------------')
        await bot.send_message(message.channel, 'The image seems to be: ' + str(bestguess))
        driver.close()

        
        

bot.run('mmsgb69@gmail.com', 'succgod123')