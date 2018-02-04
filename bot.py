import discord
import asyncio
import random
import time

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:",client.user.name)
    print("ID:",client.user.id)
    print("----------------------------------------")
    print("Auth is ready to take commands.")

@client.command
async def on_message(message):
    if message.content.startswith("a.london"):
        await client.send_message(message.channel,"https://www.roblox.com/games/883338831/City-of-London-United-Kingdom")

client.run("my_token")
