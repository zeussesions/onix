import discord
from discord.ext import commands
from discord import app_commands




class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents=discord.Intents.all()
        intents.message_content = True

    @commands.hybrid_command(name='test', with_app_command = True, description = "test")
    @app_commands.guilds()
    async def test(self, ctx: commands.Context):
        await ctx.defer(ephemeral=True)
        await ctx.reply("hi")



async def setup(bot):
    await bot.add_cog(test(bot))