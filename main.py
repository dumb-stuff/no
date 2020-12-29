import discord
from time import sleep
import os

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == "finally-verification" and message.content != "":
        sleep(7)
        await message.channel.purge(limit=1)
    if str(message.channel) == "finally-verification" and message.content != ";verify":
      return

client.run(os.getenv('TOKEN')) 