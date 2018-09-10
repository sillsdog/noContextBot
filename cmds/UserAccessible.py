import discord
from discord.ext import commands

class UserAccessible: 
    @client.command(pass_context=True)
    async def version(self,ctx):
        await ctx.send("Version: " + CurrentVersion)

    @client.command(pass_context=True)
    async def about(self,ctx):
        message = ctx.message
        await client.send_message(message.author,open('text/discordhelp.txt').read())

def setup(bot):
    bot.add_cog(UserAccessible(bot))
