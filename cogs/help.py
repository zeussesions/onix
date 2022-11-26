import discord
from discord.ext import commands
from discord import app_commands



class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents=discord.Intents.all()
        intents.message_content = True

    @commands.hybrid_command(name='help', with_app_command = True, description = "help")
    @app_commands.guilds()
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(title="Help menu!", description='onix does lots of things. Use prefix "o.', color=000000)
        embed.add_field(name="o.test", value="responds with thew ord ping", inline=False)
        embed.add_field(name="o.kiss", value="kisses any user in the server", inline=False)
        embed.add_field(name="o.hug", value="hugs any user in the server", inline=False)
        embed.add_field(name="o.shlong", value="go ahead. find out.", inline=False)
        embed.add_field(name="o.highfive", value="high fives any user in the server", inline=False)
        embed.add_field(name="o.splash", value="displays a random minecraft splash text!", inline=False)
        embed.add_field(name="o.pizzer", value="go ahead. find out.", inline=False)
        embed.add_field(name="o.crack <4 character code here>", value="uses a brute force password cracker to guess the code you put in.", inline=False)
        embed.add_field(name="o.pokemon <pokemon name or number>", value="pokemon stats!!!", inline=False)
        embed.add_field(name="o.hangman", value="Coming soon!", inline=False)
        embed.add_field(name="o.help", value="displays this embed", inline=True)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))