import discord
from discord.ext import commands
from discord import app_commands
import datetime
from datetime import timedelta
import json
import random

today_day = str(datetime.datetime.today().day)
today_month = str(datetime.datetime.today().month)


filename = "databases/holidays.json"
f = open(filename)
data = json.load(f)



class holidays(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name='holidays', with_app_command=True)
    async def holidays(self, ctx: commands.Context, date: str):
        if date == "today":
            date = f"{today_month}/{today_day}"
        elif "-" or "." or "," in date:
            date = date.replace("-", "/")
            date = date.replace(",", "/")
            date = date.replace(".", "/")
        
        embed = discord.Embed(title=f"National holidays for {date}", description="\n".join(data[date]), color=000000)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(holidays(bot))