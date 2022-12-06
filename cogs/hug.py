import discord
from discord.ext import commands
from discord import app_commands

class hug(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name='hug', with_app_command=True)
    async def hug(self, ctx: commands.Context, who: str):
        await ctx.send(str(ctx.author) + ' hugs ' + str(who) + '!\n')
        await ctx.send(file=discord.File('images/hug.gif'))

async def setup(bot):
    await bot.add_cog(hug(bot))