import discord
import nDnDICE
import os

client = discord.Client()

TOKEN = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Botを起動しました。')

@client.event
async def on_message(message):
    msg = message.content
    result = nDnDICE.nDn(msg)
    if result is not None:
        await client.send_message(message.channel, result)
    
#ここにbotのアクセストークンを入力
client.run(TOKEN)
