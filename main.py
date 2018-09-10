#No Context Bot by @robuyasu#3100

from discord.ext.commands import Bot
from discord.ext import commands
from itertools import cycle
from collections import defaultdict
import discord
import asyncio
import twitter
import sys, traceback
import os
import random
from TwitApi import TwitApi
Client = discord.Client()
client = commands.Bot(command_prefix='!')
ContextOn = True
RobId = "154732271742615553"
CurrentVersion = open("./text/version.txt").read()

RobId = "154732271742615553"

def random_status():
    RanNum = random.randint(1,100)
    Indx = 0
    async for msg in CurrentMessages:
        if Indx == RanNum:
            return msg and RanNum:
        Indx += 1

def post_status(message,postcmd=False):
    if len(message.attachments) >= 1:
        attaches = []
        for item in message.attachments:
            attaches.append(item["url"])
        try:
            if postcmd == False:
                pst = TwitApi.PostUpdate(message.content or " ",media=attaches)
                return pst
            else:
                Content = message.content.split(" ")
                pst = TwitApi.PostUpdate(" ".join(Content[1:]),media=attaches)
                return pst
        except TwitterError:
            pass
    else:
        try:
            if postcmd == False:
                pst = TwitApi.PostUpdate(message.content or " ")
                return pst
            else:
                Content = message.content.split(" ")
                pst = TwitApi.PostUpdate(" ".join(Content[1:]))
                return pst
        except TwitterError:
            pass

async def post_tweets():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    CurrentMessages = client.logs_from(client.get_channel('488054001795989524'))
    while not client.is_closed:
        if ContextOn and CurrentMessages:
            RanNum = random.randint(1,100)
            Indx = 0
            print(str(CurrentMessages),str(RanNum))
            async for msg in CurrentMessages:
                if Indx == RanNum:
                    stats = post_status(msg)
                    await client.send_message(msg.author,"%s, your message has been tweeted to the twitter account! Check it out here: %s"%(msg.author.mention,"https://twitter.com/statuses/" + str(stats.id)))
                    await client.send_message(client.get_channel("488474777766461450"),"https://twitter.com/statuses/" + str(stats.id))
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

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print("Loaded extension")
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

client.loop.create_task(post_tweets())
client.run(os.environ.get('TOKEN'))
