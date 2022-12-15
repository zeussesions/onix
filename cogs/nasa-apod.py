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

    @commands.hybrid_command(name='apod', with_app_command=True)
    async def splash(self, ctx: commands.Context, value: str):
        if value == "today":
            request = requests.get(
            'https://api.nasa.gov/planetary/apod?api_key=cOlrrCGOhdhhlJHDa69Sf4ift5a4jPGZo8qmn844')
            title = str(request.json()["title"])
            url = str(request.json()["url"])
            description = str(request.json()["explanation"])

            embed = discord.Embed(title=title, colour=discord.Color.purple())
            embed.set_image(url=url)
            embed.add_field(name="Description: ", value=description)
            await ctx.send(embed=embed)

        elif value == "random":
            randomDate = str(fake.date_between(start_date=datetime(1995,6,16), end_date='now'))
            request = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=cOlrrCGOhdhhlJHDa69Sf4ift5a4jPGZo8qmn844&date={randomDate}')
            title = str(request.json()["title"])
            url = str(request.json()["url"])
            date = str(request.json()["date"])
            description = str(request.json()["explanation"])

            embed = discord.Embed(title=title, colour=discord.Color.purple())
            embed.set_image(url=url)
            embed.add_field(name="Date: ", value=date)
            embed.add_field(name="Description: ", value=description)
            await ctx.send(embed=embed)
        
        elif "," or "/" in value:
            date = value.replace("/", "-")
            date = value.replace(",", "-")
            request = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=cOlrrCGOhdhhlJHDa69Sf4ift5a4jPGZo8qmn844&date={date}')
            if "code" in request.json():
                await ctx.send(request.json()["msg"], ephemeral=True)
            else:
                title = str(request.json()["title"])
                url = str(request.json()["url"])
                description = str(request.json()["explanation"])

                embed = discord.Embed(title=title, colour=discord.Color.purple())
                embed.set_image(url=url)
                embed.add_field(name="Description: ", value=description)
                await ctx.send(embed=embed)
            
        elif value == None:
            await ctx.send('need help? "random" gives you the image from a random day. entering a specific date will give you the image from that date. (duh) today, again, duh, gives you the image from today.' )

        else:
            await ctx.reply("invalid argument", ephemeral=True)



async def setup(bot):
    await bot.add_cog(apod(bot))