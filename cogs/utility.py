import discord
from discord.ext import commands
from discord import app_commands

class Survey(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility cog loaded, sync command online')

    @commands.command()
    @commands.guild_only()
    async def sync(self, ctx) -> None:
            synced = await ctx.bot.tree.sync()
            await ctx.send(
                f"Synced {len(synced)} commands to the current guild."
            )
            return

    @commands.hybrid_command(name='ping', with_app_command=True)
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong", ephemeral=True)
    
    @commands.hybrid_command(name='help', with_app_command=True)
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
    await bot.add_cog(Survey(bot), guilds=[discord.Object(id=874842871801479208)])