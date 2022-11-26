import discord
from discord.ext import commands
from discord import app_commands


class highfive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='highfive', with_app_command = True, description = "highfive")
    @app_commands.guilds()
    async def highfive(self, ctx: commands.Context, who):
        await ctx.send(str(ctx.author) + ' high fives ' + str(who) + '!')
        await ctx.send(file=discord.File('images/highfive.gif'))

async def setup(bot):
    await bot.add_cog(highfive(bot))