#No Context Bot by @robuyasu#3100
#Version 1.3.0

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
            if ContextOn:
                TMinus = "Posting in %s minute(s)" % (10-i)
                await client.change_presence(game=discord.Game(name=TMinus))
                await asyncio.sleep(60)

@client.event
async def on_ready():
    print("No Context Bot has been started up. To stop the program, say !bootdown . Version 1.3.0")

@client.event
async def on_message(message):
    if message.channel.id == "488054001795989524" and message.author.id != "488144253630021651" and not message.content.startswith("!") and len(message.content) >= 1 :
        CurrentMessages.append(message)
    await client.process_commands(message) #Makes sure to process the command

@client.command(pass_context=True)
async def bootup(ctx,*args):
    message = ctx.message
    if message.author.id == RobId:
        ContextOn = True
        await client.say("Successfully booted up.")
    else:
        await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

@client.command(pass_context=True)
async def bootdown(ctx,*args):
    message = ctx.message
    if message.author.id == RobId:
        ContextOn = False
        await client.say("Successfully booted down.")
    else:
        await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

@client.command(pass_context=True)
async def post(ctx,*args):
    message = ctx.message
    if message.author.id == RobId:
        await client.say("Posting message..")
        post = post_status(message,postcmd=True)
        await client.say(str(post))
        await client.say("Posted message to twitter!")
    else:
        await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

@client.command(pass_context=True)
async def version(ctx,*args):
    await client.say("Version: 1.3.0")

@client.command(pass_context=True)
async def about(ctx,*args):
    message = ctx.message
    await client.send_message(message.author,open('discordhelp.txt').read())

@client.command(pass_context=True)
async def ppost(ctx,*args):
    message = ctx.message
    if message.author.id == RobId:
        content = ctx.message.content.split(" ")
        await client.say(" ".join(content))
        await client.say(str(ctx.message.attachments) )
    else:
        await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

client.loop.create_task(post_tweets())
client.run(os.environ.get('TOKEN'))
