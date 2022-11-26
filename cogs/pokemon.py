import discord
from discord.ext import commands
from discord import app_commands
from pokedex import pokedex
import random



class pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='pokemon', with_app_command=True, description="Get a pokemon form the pokedex!")
    @app_commands.guilds()
    async def pokemon(self, ctx: commands.Context, id_or_name):
        from urllib.request import Request, urlopen
        from pokedex import pokedex
        import json
        import matplotlib

        p = pokedex.Pokedex()

        if type(id_or_name) == str:
            poke = p.get_pokemon_by_name(id_or_name)
        elif type(id_or_name) == int:
            poke = p.get_pokemon_by_number(id_or_name)

        def statsInfo(value):
            url = f"https://pokeapi.co/api/v2/pokemon/{value}"
            request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            webpage = urlopen(request_site).read()
            data = json.loads(webpage)
            return data

        def colorhex(value):
            url = f"https://pokeapi.co/api/v2/pokemon-species/{value}/"
            request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            webpage = urlopen(request_site).read()
            colorValue = json.loads(webpage)
            str = matplotlib.colors.cnames[colorValue["color"]["name"]][1:]
            base16INT = int(str, 16)
            hex_value = hex(base16INT)
            return int(hex_value, 16)

        name = poke[0]["name"]
        number = poke[0]["number"]
        height = poke[0]["height"]
        weight = poke[0]["weight"]
        types = ", ".join(poke[0]["types"])
        hp = statsInfo(id_or_name)["stats"][0]["base_stat"]
        description = poke[0]["description"]
        sprite = poke[0]["sprite"]

        embed = discord.Embed(color=colorhex(id_or_name))
        embed.add_field(name="Name: ", value=name)
        embed.add_field(name="ID: ", value=number)
        embed.add_field(name="Height: ", value=height)
        embed.add_field(name="Weight: ", value=weight)
        embed.add_field(name="Health: ", value=hp)
        embed.add_field(name="Types: ", value=types)
        embed.add_field(name="Description: ", value=description)
        embed.set_thumbnail(url=sprite)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(pokemon(bot))