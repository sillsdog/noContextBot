import discord
from discord.ext import commands
import asyncio
import twitter
from TwitApi import TwitApi

RobId = "154732271742615553"

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

class ClientOwnerOnly:
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def bootup(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            ContextOn = True
            await self.client.say("Successfully booted up.")
        else:
            await self.client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @commands.command(pass_context=True)
    async def bootdown(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            ContextOn = False
            await self.client.say("Successfully booted down.")
        else:
            await self.client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @commands.command(pass_context=True)
    async def post(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            await self.client.say("Posting message..")
            post = post_status(message,postcmd=True)
            await self.client.say(str(post))
            await self.client.say("Posted message to twitter!")
        else:
            await self.client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @commands.command(pass_context=True)
    async def ppost(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            content = ctx.message.content.split(" ")
            await self.client.say(" ".join(content))
            await self.client.say(str(ctx.message.attachments) )
        else:
            await self.client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @commands.command(pass_context=True)
    async def getmessages(self,ctx):
        msgs =  self.client.logs_from(self.client.get_channel('488054001795989524'))
        print(str(msgs))

def setup(client):
    client.add_cog(ClientOwnerOnly(client))
