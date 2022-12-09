import discord
from discord.ext import commands
from discord import app_commands
import random

class splash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name='splash', with_app_command=True)
    async def splash(self, ctx: commands.Context):
        lines = open('databases/splashes.txt').read().splitlines()
        myline = random.choice(lines)
        await ctx.send(str(myline))

async def setup(bot):
    await bot.add_cog(splash(bot))