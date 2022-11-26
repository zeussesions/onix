import discord
from discord.ext import commands
from discord import app_commands
import time

guesses = 0
guess = 0

done = False


class crack(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        intents = discord.Intents.all()
        intents.message_content = True

    @commands.hybrid_command(name='crack',
                             with_app_command=True,
                             description="crack a 4 character code")
    @app_commands.guilds()
    async def crack(self, ctx: commands.Context, code):
        if len(code) != 4:
            await ctx.send("Please enter a 4 character code.")
        else:

            await ctx.send("cracking...")

            def cracker(password):
                guessing = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                    '+', '=', '~', '`'
                ]
                ones = -1
                tens = 0
                hundreds = 0
                thousands = 0

                legnth = len(guessing)
                global guesses
                guesses = 0
                while True:
                    ones += 1
                    if ones == legnth:
                        ones = 0
                        tens += 1
                    if tens == legnth:
                        tens = 0
                        hundreds += 1
                    if hundreds == legnth:
                        hundreds = 0
                        thousands += 1
                    if thousands == legnth:
                        ones = 0
                        tens = 0
                        hundreds = 0
                        thousands = 0

                        time.sleep(0.001)

                    guess = str(guessing[thousands]) + str(
                        guessing[hundreds]) + str(guessing[tens]) + str(
                            guessing[ones])

                    guesses += 1

                    if guess == password:

                        return [guess, guesses]

            print(cracker(code))
            send = str("Your password is: " + str(cracker(code)[0]) + '\n' +
                       str(cracker(code)[1]) + " guesses")
            await ctx.send(send)
            print(guesses)


async def setup(bot):
    await bot.add_cog(crack(bot))
