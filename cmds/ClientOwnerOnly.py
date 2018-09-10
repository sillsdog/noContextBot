import discord
from discord.ext import commands

class ClientOwnerOnly:
    def __init__(self,bot):
        self.bot = bot

    @client.command(pass_context=True)
    async def bootup(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            ContextOn = True
            await client.say("Successfully booted up.")
        else:
            await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @client.command(pass_context=True)
    async def bootdown(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            ContextOn = False
            await client.say("Successfully booted down.")
        else:
            await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @client.command(pass_context=True)
    async def post(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            await client.say("Posting message..")
            post = post_status(message,postcmd=True)
            await client.say(str(post))
            await client.say("Posted message to twitter!")
        else:
            await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

    @client.command(pass_context=True)
    async def ppost(self,ctx):
        message = ctx.message
        if message.author.id == RobId:
            content = ctx.message.content.split(" ")
            await client.say(" ".join(content))
            await client.say(str(ctx.message.attachments) )
        else:
            await client.say("You do not have the permissions to do that, %s!" % (message.author.mention))

def setup(bot):
    bot.add_cog(ClientOwnerOnly(bot))
