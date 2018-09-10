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

class ModeratorOnly:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def kick(self, ctx, member: discord.Member):
        if IsMod(ctx.message.author) and ctx.message.author is not member:
            await self.client.kick(member)
            await self.client.say(member.mention + " has been kicked.")

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount: int = 50):
        if IsMod(ctx.message.author):
            await self.client.purge_from(ctx.message.channel,limit=amount)
            await self.client.say("Successfully purged %s messages." % (amount) )

    @commands.command(pass_context=True)
    async def ban(self, ctx, member: discord.Member, days: int = 1):
        if IsMod(ctx.message.author) and ctx.message.author is not member:
            await self.client.ban(member,days)
            await self.client.say("%s has been banned for %s days." % (member.mention,str(days)) )   

def setup(client):
    client.add_cog(ModeratorOnly(client))

    
