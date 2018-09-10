import discord
from discord.ext import commands

class ClientOwnerOnly:
    def __init__(self,client):
        self.client = client

    @client.command(pass_context=True)
    async def bootup(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            ContextOn = True
            await ctx.send("Successfully booted up.")
        else:
            await ctx.send("You do not have the permissions to do that, %s!" % (message.author.mention))

    @client.command(pass_context=True)
    async def bootdown(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            ContextOn = False
            await ctx.send("Successfully booted down.")
        else:
            await ctx.send("You do not have the permissions to do that, %s!" % (message.author.mention))

    @client.command(pass_context=True)
    async def post(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            await ctx.send("Posting message..")
            post = post_status(message,postcmd=True)
            await ctx.send(str(post))
            await ctx.send("Posted message to twitter!")
        else:
            await ctx.send("You do not have the permissions to do that, %s!" % (message.author.mention))

    @client.command(pass_context=True)
    async def ppost(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            content = ctx.message.content.split(" ")
            await ctx.send(" ".join(content))
            await ctx.send(str(ctx.message.attachments) )
        else:
            await ctx.send("You do not have the permissions to do that, %s!" % (message.author.mention))

def setup(client):
    client.add_cog(ClientOwnerOnly(client))
