import random
import time

import discord
from discord.ext import commands


class rng(commands.Cog):
    def __init__(self, client):
        self.client = client

    # event
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot RNG Cog is loaded")

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it.",
        ]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    # flips a coin
    @commands.command()
    async def cf(self, ctx):
        random.seed(time.time())
        coin = random.choice(["Heads", "Tails"])
        await ctx.send(f"{coin}")

    # generates a random number from min to max (enclusive)
    @commands.command()
    async def rand(self, ctx, min=1, max=10):
        random.seed(time.time())
        num = str(random.randint(int(min), int(max)))
        await ctx.send(num)

    # generates a random float between 0 and 1 (enclusive)
    @commands.command()
    async def float(self, ctx):
        random.seed(time.time())
        await ctx.send(random.random())


def setup(client):
    client.add_cog(rng(client))
