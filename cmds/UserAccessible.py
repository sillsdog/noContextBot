import discord
from discord.ext import commands
import asyncio
import twitter
from TwitApi import TwitApi

class UserAccessible: 
    def __init__(self,client):
        self.client = client        

    @commands.command(pass_context=True)
    async def version(self,ctx):
        await self.client.say("Version: " + open('text/version.txt').read())

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        await self.client.say("Pong!")

    @commands.command(pass_context=True)
    async def about(self,ctx):
        message = ctx.message
        await self.client.send_message(message.author,open('text/discordhelp.txt').read())

    @commands.command(pass_context=True)
    async def searchtwitter(self,ctx, id: str = ""):
        if id is None:
            self.client.say("Please enter a valid twitter status ID.")
        Status = TwitApi.GetStatus(id)
        if Status:
            self.client.say("https://twitter.com/statuses/" + str(Status.id))
        else:
            self.client.say("Search Twitter by ID failed!")

def setup(client):
    client.add_cog(UserAccessible(client))
