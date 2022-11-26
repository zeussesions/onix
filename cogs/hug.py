import discord
from discord.ext import commands
from discord import app_commands

class hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='hug', with_app_command = True, description = "hug")
    @app_commands.guilds()
    async def hug(self, ctx, who):
        await ctx.send(str(ctx.author) + ' hugs ' + str(who) + '!\n')
        await ctx.send(file=discord.File('images/hug.gif'))

async def setup(bot):
    await bot.add_cog(hug(bot))