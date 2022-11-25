import os
import random

import discord
from discord.ext import commands

NAME = "OttBot V2.0"
ID = "785990964916518950"

client = commands.Bot(command_prefix="./")


@client.event
async def on_ready():
    print("Bot online")


# ==============================================================================
# Join and leave events
# ==============================================================================

@client.event
async def on_member_join(member):
    """Send custom join message."""
    print(f"{member} has joined the server.")


@client.event
async def on_member_remove(member):
    """Send custom leave message"""
    print(f"{member} has left the server.")



# ==============================================================================
# Help commands
# ==============================================================================

@client.command(aliases=['help', 'h'])
async def help(ctx):
    ctx.send("")


# ==============================================================================
# Bot tool commands
# ==============================================================================

@client.command()
async def load(ctx, extension):
    """Load cogs."""
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} was loaded")


@client.command()
async def unload(ctx, extension):
    """Unloads cogs."""
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} was unloaded")


@load.error
async def info_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("That extension is already unloaded.")


"""
Test commands
"""
# test
@client.command(aliases=["lmao", "lamo"])
async def test(ctx):
    await ctx.send("test")


# pings the bot
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


"""
Server tool commands
"""

# Chat Clear
@client.command()
async def clear(ctx, amount=5):
    if amount > 100:
        await ctx.send(f"{amount} is too many, (100 max)")
    else:
        await ctx.channel.purge(limit=amount + 1)


# Kick user
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")


# Ban User
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")


# Unban user
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
async def twerk(ctx):
    await ctx.send("https://tenor.com/view/peepeepoopoo-gif-18294063")


"""
RNG commands
"""
"""
#responds to a question with a 8-ball response
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.",
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


#flips a coin
@client.command()
async def cf(ctx):
    coin = random.choice(["Heads", "Tails"])
    await ctx.send(f'{coin}')

#generates a random number from min to max (enclusive)
@client.command()
async def rand(ctx, min, max):
    num = random.randint(int(min),int(max))
    await ctx.send(num)

#generates a random float between 0 and 1 (enclusive)
@client.command()
async def float(ctx):
    await ctx.send(random.random())
"""


default_unloaded_cogs_list = ["rng.py"]

for filename in os.listdir("./cogs"):
    if (
        filename.endswith(".py")
        and filename != "info.py"
        and filename not in default_unloaded_cogs_list
    ):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(os.environ["TOKEN"])
