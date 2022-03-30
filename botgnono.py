import discord
from discord import guild
from discord import member
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import asyncio

client = commands.Bot(command_prefix= "?")
client.remove_command("help")

@client.event
async def on_ready():
    print("bot online")
    await client.change_presence(activity=discord.Game(name="energycraft"))



@client.command()
async def no(ctx):
   await ctx.send("no")
   await ctx.send("no")
   await ctx.send("no")
   await ctx.send("no")
   await ctx.send("no")


@client.command()
async def info_edycja(ctx):
   await ctx.send("start edycji: prawdopodobnie 2.04.2022")
   

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason="bez powodu"):
        await member.kick(reason=reason)
        await ctx.channel.send(f"Wyrzucony: {member.mention} za: {reason}")


@client.command()
@has_permissions(kick_members=True)
async def ban(ctx, member : discord.Member, reason="bez powodu"):
        await member.kick(reason=reason)
        await ctx.channel.send(f"zbanowany: {member.mention} za: {reason}")


@client.command()
async def emoji(ctx):
    tablica = ["👑", "💥", "🤬", "🤖","🧶"]
    await ctx.channel.send(random.choice(tablica))


@client.command()
@has_permissions(kick_members=True)
async def clear(ctx, ilosc=1000):
    await ctx.channel.purge(limit=ilosc)
    await ctx.send("pomyślnie usunięto")
    

client.run("OTUzNzY1Nzc5MDkyOTQyODQ4.YjJVmQ.Uewhzvpr9ekKi33et3UrLqQwE7k")
