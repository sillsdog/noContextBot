import discord
from discord.ext import commands
import asyncio

class UserAccessible: 
    def __init__(self,client):
        self.bot = client

    @commands.command(pass_context=True)
    async def version(self,ctx):
        await ctx.send("Version: 1.3.2")

    #@commands.command(pass_context=True)
    #async def about(self,ctx):
    #    message = ctx.message
    #    await client.send_message(message.author,open('text/discordhelp.txt').read())

def setup(client):
    client.add_cog(UserAccessible(client))
