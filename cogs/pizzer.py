import discord
from discord.ext import commands
from discord import app_commands


class pizzer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        intents.message_content = True

    @commands.hybrid_command(name='pizzer', with_app_command=True)
    async def pizzer(self, ctx: commands.Context):
        await ctx.send(file=discord.File('images/pizzer.gif'))


async def setup(bot):
    await bot.add_cog(pizzer(bot))
