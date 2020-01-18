import discord 
import os
import asyncio
import random
from datetime import datetime


#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

CHANNEL_ID = 665579602504318978

#起動メッセージ
@client.event
async def on_ready():
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('Hello World,『Discord-Test-Program』通称「DTP」、起動しました')
    channel = client.get_channel(CHANNEL_ID)
    await channel.purge()
    await channel.send(f'名前:{client.user.name}')  # ボットの名前
    await channel.send(f'ID:{client.user.id}')  # ボットのID
    await channel.send(f'Discord ver:{discord.__version__}')  # discord.pyのバージョン
    await channel.send('----------------')
    await channel.send('状態：DTP起動しました。')   
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='DTP起動'))    

@client.event
async def on_message(message):
    
    if message.author.bot:  # ボットを弾く。
        return 
    if message.content == 'roll':
        role1 = discord.utils.get(message.guild.roles, name='class SAXONY')
        await guild.create_roles(role1)


client.run(TOKEN)
