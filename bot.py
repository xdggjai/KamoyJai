import os
import discord
from discord import app_commands
from discord.ext import commands
from server import server_on

bot = commands.Bot(command_prefix = "!",intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

@bot.event
async def on_message(message):
    mes = message.content
    if mes == "hello":
        await message.channel.sent("Hello It's me")
    elif mes == "hi bot":
        await message.channel.send("Hello, " + str(message.author.name))
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}")

@bot.command()
async def test(ctx,arg):
    await ctx.semd(arg)

@bot.tree.command(name = "hellobot",description = "Replies with Hello")
async def hellocomand(interaction):
    await interaction.response.sent_message("Hello It's me BOT DISCORD")

##@bot.tree.command(name = "name")
##@app_commands.describe(name = "What's your name?")
##async def namecommand(interaction,name):
##    await interaction.response.send_message(f"Hello {name}")

server_on()

bot.run(os.getenv("TOKEN"))
