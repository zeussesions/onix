import discord
import asyncio
import os
from discord.ext import commands
import json

with open("config.json") as f:
    data = json.load(f)
    TOKEN = data["TOKEN"]
    PREFIX = data["PREFIX"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, application_id='1024728796127039548')


bot.remove_command("help")
bot.remove_command("ping")

@bot.event
async def on_ready():

    print('bot is online')


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())