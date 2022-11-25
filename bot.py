import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

NAME = "OttBot V2.0"
ID = "785990964916518950"

client = commands.Bot(command_prefix="./", intents=discord.Intents.all())


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

# Discord.py comes with a default help command
# @client.command(aliases=["help", "h"])
# async def help(ctx):
#     ctx.send("")


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


# ==============================================================================
# Test commands
# ==============================================================================


@client.command(aliases=["lmao", "lamo"])
async def test(ctx):
    """Test."""
    await ctx.send("test")


@client.command()
async def ping(ctx):
    """Pings the bot."""
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


# ==============================================================================
# Server tool commands
# ==============================================================================


@client.command()
async def clear(ctx, amount=5):
    """Clear chat."""
    if amount > 100:
        await ctx.send(f"{amount} is too many, (100 max)")
    else:
        await ctx.channel.purge(limit=amount + 1)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    """Kick a user."""
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    """Ban a user."""
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")


@client.command()
async def unban(ctx, *, member):
    """Unban a user."""
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


# ==============================================================================
# Load cogs and run the bot
# ==============================================================================


default_unloaded_cogs_list = ["rng.py"]

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename not in default_unloaded_cogs_list:
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(os.environ["TOKEN"])
