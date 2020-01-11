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
        date = datetime.now()
        my_message = await message.channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        await asyncio.sleep(1)
        await my_message.edit(content=f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        await asyncio.sleep(1)
        await my_message.edit(content=f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        await asyncio.sleep(1)
        await my_message.edit(content=f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        await asyncio.sleep(1)
        await my_message.edit(content=f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        await asyncio.sleep(1)
        await my_message.edit(content=f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        await asyncio.sleep(1)
        await my_message.edit(content=f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')
        
@tasks.loop(seconds=5)
async def loop():
    await channel.purge()
    channel = client.get_channel(665641489975607297)
    date = datetime.now()
    await channel.send(f'{date.hour}：{date.minute}：{date.second}') 

#ループ処理実行
loop.start()

client.run(TOKEN)
