import discord
from discord.ext import commands
from discord import app_commands
import random
import re

class rolladice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        intents=discord.Intents.all()
        intents.message_content = True

    @commands.hybrid_command(name='rolladice', with_app_command=True)
    async def rolladice(self, ctx: commands.Context, dice: str):
        
        temp = re.findall(r'\d+', dice)
        res = list(map(int, temp))
        
        rolls = []
                
        for i in range(res[0]):
            rolls.append(random.randint(1, res[1]))
        
        await ctx.send(sum(rolls), ephemeral=True)

async def setup(bot):
    await bot.add_cog(rolladice(bot))