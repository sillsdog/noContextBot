import discord
from discord.ext import commands
import asyncio

class UserAccessible: 
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def version(self,ctx):
        await self.client.say("Version: 1.3.2")

    @commands.command(pass_context=True)
    async def about(self,ctx):
        message = ctx.message
        await self.client.send_message(message.author,open('text/discordhelp.txt').read())

def setup(client):
    client.add_cog(UserAccessible(client))
