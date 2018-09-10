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
client = commands.Bot(command_prefix='!',max_messages=100)
ContextOn = True
RobId = "154732271742615553"
CurrentVersion = open("./text/version.txt").read()

RobId = "154732271742615553"

def post_status(message,postcmd=False):
    if len(message.attachments) >= 1:
        attaches = []
        for item in message.attachments:
            attaches.append(item["url"])

        if postcmd == False:
            pst = TwitApi.PostUpdate(message.content or " ",media=attaches)
            return pst
        else:
            Content = message.content.split(" ")
            pst = TwitApi.PostUpdate(" ".join(Content[1:]),media=attaches)
            return pst
    else:
        if postcmd == False:
            pst = TwitApi.PostUpdate(message.content or " ")
            return pst
        else:
            Content = message.content.split(" ")
            pst = TwitApi.PostUpdate(" ".join(Content[1:]))
            return pst

async def post_tweets():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    CurrentMessages = client.messages
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
