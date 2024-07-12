import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
    guild = bot.get_guild(1247621044785774653)
    print(f"Bot is ready! on {guild.name}")

@bot.command()
async def synccmd(ctx):
    fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    await ctx.send(f"Syncd {len(fmt)} commands to the current server")

@bot.event
async def on_member_join(member):
    print("{} joined the server".format(member))

@bot.event
async def on_member_remove(member):
    print("{} left the server".format(member))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(bot.latency * 1000)))

@bot.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    answers = [
        "It is Certain.", "It is decidedly so.", "Without a doubt.",
        "Yes definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.",
        "Don't count on it.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful."
    ]
    await ctx.send("Question: {}?\nAnswer: {}".format(question, random.choice(answers)))

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def meow_all_dm(ctx):
    members = ctx.guild.members
    for member in members:
        if member == bot.user:
            continue
        try:
            for i in range(20):
                await member.send(f"meow")
            await ctx.send(
                f"Successfully sent to {member.name}#{member.discriminator}")
        except:
            await ctx.send(f"Couldnt send to {member.name}#{member.discriminator}")

@bot.command()
async def meow_all(ctx):
    members = ctx.guild.members
    for member in members:
        if member.bot:  # Skip the bot itself and other bots
            continue
        try:
            for i in range(20):
                await ctx.send(f"meow {member.mention}")
            await ctx.send(
                f"Successfully sent to {member.name}#{member.discriminator}")
        except:
            await ctx.send(f"Couldn't send to {member.name}#{member.discriminator}")

@bot.tree.command(name="coinflip", description="Flips a coin")
async def coin_flip(interaction: discord.Integration):
    await interaction.response.send_message(random.choice(['Heads', 'Tails']))

@bot.command()
async def listcmds(ctx):
    commands_list = [f"{command.name}" for command in bot.commands]
    await ctx.send("Available Commands:\n" + "\n".join(commands_list))

token = os.environ["DISCORD_TOKEN"]

bot.run(token)
