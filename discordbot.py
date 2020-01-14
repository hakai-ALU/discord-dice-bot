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
        
    if message.content.startswith("スロット"): 
        suroto=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
        suroto1=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
        suroto2=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
        await asyncio.sleep(0.1)
        my_message = await message.channel.send('スロット結果がここに表示されます！')
        await asyncio.sleep(3)
        await my_message.edit(content='？|？|？')
        await asyncio.sleep(1)
        await my_message.edit(content=suroto + '|？|？')
        await asyncio.sleep(1)
        await my_message.edit(content=suroto + '|' + suroto1 + '|？')
        await asyncio.sleep(1)
        await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2)
        if suroto == suroto1 == suroto2:
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：大当たり！！')
        elif suroto == suroto1 or suroto == suroto2 or suroto1 == suroto2:
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：リーチ！')
        else:
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：ハズレ')
        
client.run(TOKEN)
