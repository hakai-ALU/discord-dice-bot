import discord 
import os
import asyncio
from discord.ext import tasks
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
    if message.content.startswith("テスト"): 
        my_message = await message.channel.send("こんにちは")
        await my_message.edit(content="こ")
        await asyncio.sleep(0.5)
        await my_message.edit(content="こん")
        await asyncio.sleep(0.5)
        await my_message.edit(content="こんば")
        await asyncio.sleep(0.5)
        await my_message.edit(content="こんばん")
        await asyncio.sleep(0.5)
        await my_message.edit(content="こんばんは")
        await asyncio.sleep(0.5)
        await my_message.edit(content="こんばんは。")
        
@tasks.loop(seconds=5)
async def loop():
    channel = client.get_channel(665641489975607297)
    my_bot_message = await channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
    date = datetime.now()
    await my_bot_message.edit(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！') 

#ループ処理実行
loop.start()

client.run(TOKEN)
