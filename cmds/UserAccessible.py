import discord
from discord.ext import commands
import asyncio

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

def setup(client):
    client.add_cog(UserAccessible(client))
