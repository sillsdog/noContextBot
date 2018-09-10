#No Context Bot by @robuyasu#3100

from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
from TwitApi import TwitApi
from twitter.error import TwitterError
import discord
import asyncio
import twitter
import sys, traceback
import os
import random
Client = discord.Client()
client = commands.Bot(command_prefix='!')
ContextOn = True
RobId = "154732271742615553"
CurrentVersion = open("./text/version.txt").read()

RobId = "154732271742615553"

def post_status(message,postcmd=False):
    if len(message.attachments) >= 1:
        attaches = []
        for item in message.attachments:
            attaches.append(item["url"])
        try:
            if postcmd == False:
                print("Touchdown")
                pst = TwitApi.PostUpdate(message.content[:250] or " ",media=attaches)
                return pst
            else:
                print("Touchdown")
                Content = message.content.split(" ")
                pst = TwitApi.PostUpdate((" ".join(Content[1:]))[:250],media=attaches)
                return pst
        except TwitterError:
            return False
    else:
        try:
            if postcmd == False:
                print("Touchdown")
                pst = TwitApi.PostUpdate(message.content[:250] or " ")
                return pst
            else:
                print("Touchdown")
                Content = message.content.split(" ")
                pst = TwitApi.PostUpdate( (" ".join(Content[1:]))[:250] )
                return pst
        except TwitterError:
            return False

async def post_tweets():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    while not client.is_closed:
        if ContextOn:
            CurrentMessages = client.logs_from(client.get_channel('488054001795989524'),limit=25)
            MsgList = []
            async for msg in CurrentMessages:
                MsgList.append(msg)
                
            ChosenMsg = random.choice(MsgList)
            stats = post_status(ChosenMsg)
            if stats:
                await client.send_message(ChosenMsg.author,"%s, your message has been tweeted to the twitter account! Check it out here: %s"%(ChosenMsg.author.mention,"https://twitter.com/statuses/" + str(stats.id)))
                await client.send_message(client.get_channel("488474777766461450"),"https://twitter.com/statuses/" + str(stats.id))
            else:
                await client.say("An error has occured in post_tweets(), client a nil value.")
        for i in range(10): #Waits for 10 minutes
            if ContextOn:
                TMinus = "Posting in %s minute(s)" % (10-i)
                await client.change_presence(game=discord.Game(name=TMinus))
                await asyncio.sleep(60)

@client.event
async def on_ready():
    print("No Context Bot has been started up. To stop the program, say !bootdown . Version " + CurrentVersion)

@client.event
async def on_message(message):
    await client.process_commands(message) #Makes sure to process the command

initial_extensions = [
    'cmds.ClientOwnerOnly',
    'cmds.ModeratorOnly',
    'cmds.UserAccessible'
]

if __name__ == '__main__': #Loads commands/extensions
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print("Loaded extension")
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

client.loop.create_task(post_tweets())
client.run(os.environ.get('TOKEN'))
