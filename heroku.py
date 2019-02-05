import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.client()
client = commands.bot(command_prefix = "$")
@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        msg = "hello (0,author.mention) how are you today".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("bye "):
        msg = "goodbye (0,author.mention) hope i see you soon!".format(message)
        await client.send_message(message.channel, msg)

    client.run(os.getenv('token'))
        
