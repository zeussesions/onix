import discord
from discord.ext import commands
from discord import app_commands


class shlong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='shlong', with_app_command=True)
    async def shlong(self, ctx: commands.Context):
        await ctx.send(file=discord.File('images/wiibowling.gif'))

async def setup(bot):
    await bot.add_cog(shlong(bot))