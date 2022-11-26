import discord
from discord.ext import commands
import os
import asyncio

import json
from keep_alive import keep_alive

with open("config.json") as f:
    data = json.load(f)
    TOKEN = data["TOKEN"]
    prefix = data["PREFIX"]


guild = discord.Object(id=1006191458920955935)
intents = discord.Intents.all()
intents.members = True

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = prefix, intents = intents)

    async def setup_hook(self):
        await self.tree.sync(guild = guild)
        print(f"synced slash commands for {self.user}")
        print("bot is online")

bot = Bot()

bot.remove_command('help')
bot.remove_command('test')
bot.remove_command('ping')


#everytrhing after this is cog loading, and the web server, for the love of god don't touch it
async def load():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    await bot.start(TOKEN)

keep_alive()
try:
    asyncio.run(main())
except:
    os.system("kill 1")
