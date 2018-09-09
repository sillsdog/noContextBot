#No Context Bot by @robuyasu#3100
#Version 1.0.0

from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
from collections import defaultdict
import discord
import asyncio
import twitter
import requests
import random
import commandsdisc

Client = discord.Client()
client = commands.Bot(command_prefix='!')

CurrentMessages = []
ContextOn = True

RobId = "154732271742615553"
TwitApi = twitter.Api(consumer_key='kEpgtAzIwc3mXuxY8lWpoiMGT',
consumer_secret='rcm2pqUj6CMiCmy1TL8PWheimxlJk9CrLcMym569i2zVbIFhba',
access_token_key='1038495867639136256-Z4Zl3k0vtD3KPe707eDEuCNpcF2geH',
access_token_secret='e8VDI74qYaXLMxqittastSR3IXDjSjKnCHuTVpvkUjvdm')

contcmds = {
    "!BOOTUP":commandsdisc.bootup,
    "!BOOTDOWN":commandsdisc.bootdown,
    "!POST":commandsdisc.post,
    "!VERSION":commandsdisc.version,
    "!ABOUT":commandsdisc.about
}

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
    if message.channel.id == "488054001795989524" and message.author.id != "488144253630021651" and not message.content.startswith("!") and len(message.content) >= 1 :
        CurrentMessages.append(message)

    for cmd,func in contcmds:
        if message.content.upper().startswith(cmd):
            func(message)




client.loop.create_task(post_tweets())
client.run('NDg4MTQ0MjUzNjMwMDIxNjUx.DnX8mQ.2l3sgx7QoU1bQAbLTH9LgwQovwI')
