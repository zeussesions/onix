import discord
from discord.ext import commands
from discord import app_commands
import requests
from datetime import datetime
from faker import Faker

fake = Faker()

class apod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='apod', with_app_command=True, description="use a 'date', formatted month-day-year, 'random', or 'today' to get the image of the day!")
    @app_commands.guilds()
    async def apod(self, ctx, value):
        if value == "today":
            request = requests.get('https://api.nasa.gov/planetary/apod?api_key=cOlrrCGOhdhhlJHDa69Sf4ift5a4jPGZo8qmn844')
            title = str(request.json()["title"])
            url = str(request.json()["url"])
            date = str(request.json()["date"])
            description = str(request.json()["explination"])

            embed = discord.Embed(title=title)
            embed.set_image(url=url)
            embed.add_field(name="Date: ", value=date)
            embed.add_field(name="Description: ", value=description)
            ctx.send(embed=embed)

        elif value == "random":
            randomDate = str(fake.date_between(start_date=datetime(1995,6,16), end_date='now'))
            request = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=cOlrrCGOhdhhlJHDa69Sf4ift5a4jPGZo8qmn844&{randomDate}')
            title = str(request.json()["title"])
            url = str(request.json()["url"])
            date = str(request.json()["date"])
            description = str(request.json()["explination"])

            embed = discord.Embed(title=title)
            embed.set_image(url=url)
            embed.add_field(name="Date: ", value=date)
            embed.add_field(name="Description: ", value=description)
            ctx.send(embed=embed)
        
        elif "-" or "/" in value:
            date = value.replace("/" "-")
            date = value.replace("," "-")
            request = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=cOlrrCGOhdhhlJHDa69Sf4ift5a4jPGZo8qmn844&{date}')
            title = str(request.json()["title"])
            url = str(request.json()["url"])
            date = str(request.json()["date"])
            description = str(request.json()["explination"])
            
            embed = discord.Embed(title=title)
            embed.set_image(url=url)
            embed.add_field(name="Date: ", value=date)
            embed.add_field(name="Description: ", value=description)
            ctx.send(embed=embed)
            

        else:
            ctx.reply("invalid argument", ephemeral=True)



async def setup(bot):
    await bot.add_cog(apod(bot))
