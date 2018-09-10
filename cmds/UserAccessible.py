import discord
from discord.ext import commands

class UserAccessible: 
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def version(self,ctx):
        await ctx.send("Version: " + CurrentVersion)

    @commands.command(pass_context=True)
    async def about(self,ctx):
        message = ctx.message
        await client.send_message(message.author,open('text/discordhelp.txt').read())

def setup(client):
    client.add_cog(UserAccessible(client))
