import discord 
import os
import nDnDICE

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('Hello World,対話botプログラム「Project-Dice-K」、起動しました')

@client.event
async def on_message(message):
    msg = message.content
    result = nDnDICE.nDn(msg)
    if result is not None:
        await client.send_message(message.channel, result)

client.run(TOKEN)
