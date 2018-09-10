#No Context Bot by @robuyasu#3100
#Version 1.2.5

from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
from collections import defaultdict
import discord
import asyncio
import twitter
import requests
import os
import random
Client = discord.Client()
client = commands.Bot(command_prefix='!')

CurrentMessages = []
ContextOn = True

RobId = "154732271742615553"
TwitApi = twitter.Api(consumer_key=os.environ.get('CONSKEY'),
consumer_secret=os.environ.get('CONSCRT'),
access_token_key=os.environ.get('ACSKEY'),
access_token_secret=os.environ.get('ACSSCRT'))

print os.environ.get('CONSKEY')
print os.environ.get('CONSCRT')
print os.environ.get('ACSKEY')
print os.environ.get('ACSSCRT')

def post_status(message,postcmd=False):
    if len(message.attachments) >= 1:
        attaches = []
        for item in message.attachments:
            attaches.append(item["url"])

        if postcmd == False:
            pst = TwitApi.PostUpdate(message.content,media=attaches)
            return pst
        else:
            Content = message.content.split(" ")
            pst = TwitApi.PostUpdate(" ".join(Content[1:]),media=attaches)
            return pst
    else:
        if postcmd == False:
            pst = TwitApi.PostUpdate(message.content)
            return pst
        else:
            Content = message.content.split(" ")
            pst = TwitApi.PostUpdate(" ".join(Content[1:]))
            return pst

async def bootup(message):
    if message.author.id == RobId:
        ContextOn = True
        await client.send_message(message.channel,"Successfully booted up.")
    else:
        await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))


async def bootdown(message):
    if message.author.id == RobId:
        ContextOn = False
        await client.send_message(message.channel,"Successfully booted down.")
    else:
        await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))


async def post(message):
    if message.author.id == RobId:
        await client.send_message(message.channel,"Posting message..")
        post = post_status(message,postcmd=True)
        await client.send_message(message.channel,str(post))
        await client.send_message(message.channel,"Posted message to twitter!")

async def version(message):
    await client.send_message(message.channel,"Version: 1.2.5")

async def about(message):
    await client.send_message(message.author,'''
Hey There! I'm No Context Bot.
I was programmed by @robuyasu#3100, and was created September 9, 2018.

My purpose is to select recent messages, and tweet one of the many random recent messages.
I am coded in Python, and hosted at heroku.

Want to view my source code or help out? View https://github.com/Robuyasu/noContextBot

    ''')

async def ppost(message):
    if message.author.id == RobId:
        await client.send_message(message.channel, message.content)
        await client.send_message(message.channel, str(message.attachments) )

contcmds = {
    "!BOOTUP":bootup,
    "!BOOTDOWN":bootdown,
    "!POST":post,
    "!VERSION":version,
    "!ABOUT":about,
    "!PPOST":ppost
}

async def post_tweets():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    while not client.is_closed:
        if ContextOn and CurrentMessages:
            if len(CurrentMessages) >= 1:
                ChosenMsg = random.choice(CurrentMessages)
                if ChosenMsg:
                    stats = post_status(ChosenMsg)
                    await client.send_message(ChosenMsg.author,"%s, your message has been tweeted to the twitter account! Check it out here: %s"%(ChosenMsg.author.mention,"https://twitter.com/statuses/" + str(stats.id)))
                    await client.send_message(client.get_channel("488474777766461450"),"https://twitter.com/statuses/" + str(stats.id))
                else:
                    print("Twit API error has occured.")
                CurrentMessages.clear()

        for i in range(10): #Waits for 10 minutes
            TMinus = "Posting in %s minute(s)" % (10-i)
            await client.change_presence(game=discord.Game(name=TMinus))
            await asyncio.sleep(60)

@client.event
async def on_ready():
    print("No Context Bot has been started up. To stop the program @robuyasu#3100 , say !bootdown . Version 1.2.5")

@client.event
async def on_message(message):
    if message.channel.id == "488054001795989524" and message.author.id != "488144253630021651" and not message.content.startswith("!") and len(message.content) >= 1 :
        CurrentMessages.append(message)

    for cmd,func in contcmds.items():
        if message.content.upper().startswith(cmd):
            await func(message)

client.loop.create_task(post_tweets())
client.run(os.environ.get('TOKEN'))
