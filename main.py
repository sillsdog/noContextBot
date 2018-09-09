#No Context Bot by @robuyasu#3100
#Version 1.0.0

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import twitter
import requests
from itertools import cycle
import random

Client = discord.Client()
client = commands.Bot(command_prefix='!')

CurrentMessages = []
ContextOn = True

loadGreetTxt = requests.get("https://pastebin.com/raw/sNEdNfAF")

RobId = "154732271742615553"
TwitApi = twitter.Api(consumer_key='kEpgtAzIwc3mXuxY8lWpoiMGT',
consumer_secret='rcm2pqUj6CMiCmy1TL8PWheimxlJk9CrLcMym569i2zVbIFhba',
access_token_key='1038495867639136256-Z4Zl3k0vtD3KPe707eDEuCNpcF2geH',
access_token_secret='e8VDI74qYaXLMxqittastSR3IXDjSjKnCHuTVpvkUjvdm')

async def post_tweets():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    while not client.is_closed:
        if ContextOn and CurrentMessages and len(CurrentMessages) >= 2:
            ChosenMsg = random.choice(CurrentMessages)
            if ChosenMsg:
                TwitApi.PostUpdate(ChosenMsg.content)
                await client.send_message(ChosenMsg.channel,"%s, your message has been tweeted to the twitter account!"%(ChosenMsg.author.mention))
            else:
                print("Twit API error has occured.")
            CurrentMessages.clear()
        for i in range(10): #Waits for 10 minutes
            TMinus = "Posting in %s minute(s)" % (10-i)
            await client.change_presence(game=discord.Game(name=TMinus))
            await asyncio.sleep(60)

@client.event
async def on_ready():
    print("No Context Bot has been started up. To stop the program @robuyasu#3100 , say !bootdown . Version 1.0.0")

@client.event
async def on_message(message):
    if message.channel.id == "488054001795989524" and message.author.id != "488144253630021651" and not message.content.startswith("!"):
        CurrentMessages.append(message)

    if message.content.upper() == "!BOOTDOWN":
        if message.author.id == RobId:
            ContextOn = False
            await client.send_message(message.channel,"Successfully booted down.")
        else:
            await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))

    elif message.content.upper() == "!BOOTUP":
        if message.author.id == RobId:
            ContextOn = True
            await client.send_message(message.channel,"Successfully booted up.")
        else:
            await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))

    elif message.content.upper().startswith("!POST"):
        if message.author.id == RobId:
            Content = message.content.split(" ")
            await client.send_message(message.channel,"Posting message..")
            TwitApi.PostUpdate(" ".join(Content[1:]))
            await client.send_message(message.channel,"Posted message to twitter!")
    elif message.content.upper() == "!VERSION":
        await client.send_message(message.channel,"Version: 1.0.0")
    elif message.content.upper() == "!ABOUT":
        await client.send_message(message.author,loadGreetTxt.Text)

client.loop.create_task(post_tweets())
client.run('NDg4MTQ0MjUzNjMwMDIxNjUx.DnX8mQ.2l3sgx7QoU1bQAbLTH9LgwQovwI')
