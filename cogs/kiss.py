import discord
from discord.ext import commands
from discord import app_commands



class kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='kiss', with_app_command=True)
    async def kiss(self, ctx: commands.Context, who: str):
        file = discord.File('images/kiss.gif')
        await ctx.send(str(ctx.author) + ' kisses ' + str(who) + '!\n')
        await ctx.send(file=discord.File('images/kiss.gif'))

async def setup(bot):
    await bot.add_cog(kiss(bot))
