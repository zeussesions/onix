import discord
from discord.ext import commands
from discord import app_commands



class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='say', with_app_command = True, description = "say")
    @app_commands.guilds()
    async def say(self, ctx: commands.Context, phrase):
        await ctx.reply(phrase)

async def setup(bot):
    await bot.add_cog(say(bot))