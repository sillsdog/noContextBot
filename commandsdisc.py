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

def bootup(message):
    if message.author.id == RobId:
        ContextOn = True
        await client.send_message(message.channel,"Successfully booted up.")
    else:
        await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))


def bootdown(message):
     if message.author.id == RobId:
        ContextOn = False
        await client.send_message(message.channel,"Successfully booted down.")
    else:
        await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))


def post(message):
    if message.author.id == RobId:
        Content = message.content.split(" ")
        await client.send_message(message.channel,"Posting message..")
        TwitApi.PostUpdate(" ".join(Content[1:]))
        await client.send_message(message.channel,"Posted message to twitter!")

def version(message):
    await client.send_message(message.channel,"Version: 1.0.0")

def about(message):
        await client.send_message(message.author,'''
Hey There! I'm No Context Bot.
I was programmed by @robuyasu#3100, and was created September 9, 2018.

My purpose is to select recent messages, and tweet one of the many random recent messages.
I am coded in Python, and hosted at heroku.

Want to view my source code or help out? View https://github.com/Robuyasu/noContextBot

        ''')
