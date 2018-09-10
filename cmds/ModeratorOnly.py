import discord
from discord.ext import commands
import asyncio
import twitter
from TwitApi import TwitApi
modroles = open("text/modroles.txt").read()
def IsMod(user):
    for role in user.roles:
        if modroles.find(role.name):
            return True
    return False

async def checkMember(self,member: discord.Member):
    if member is None:
        await self.client.say("Invalid username.")
        return

class ModeratorOnly:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def kick(self, ctx, member: discord.Member):
        checkMember(self,member)
        if IsMod(ctx.message.author) and ctx.message.author is not member:
            await self.client.kick(member)
            await self.client.say(member.mention + " has been kicked.")

    @commands.command(pass_context=True)
    async def mute(self, ctx, member: discord.Member):
        checkMember(self,member)
        if IsMod(ctx.message.author) and ctx.message.author is not member:
            await self.client.mute(member)
            await self.client.say(member.mention + " has been muted.")

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount: int = 50):
        if IsMod(ctx.message.author):
            await self.client.purge_from(ctx.message.channel,limit=amount)
            await self.client.say("Successfully purged %s messages." % (amount) )

def setup(client):
    client.add_cog(ModeratorOnly(client))

    
