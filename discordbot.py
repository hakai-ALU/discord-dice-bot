import discord 
import os
from discord.ext import tasks
from datetime import datetime
import random
import re

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 587658526013390859 #チャンネルID
CHANNEL_ID2 = 603203288883789831
CHANNEL_ID3 = 604573398831726602

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    print('Hello World,リマインドbotプログラム「project-remain」、起動しました')
    channel = client.get_channel(CHANNEL_ID2)
    await channel.send('BOT再起動しました。')   

@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return
    
    if message.content == "おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '中吉', '小吉', '吉', '半吉', '末吉', '末小吉', '凶', '小凶', '半凶', '末凶', '大凶')), inline=False)
        await client.get_channel(CHANNEL_ID3).send(embed=embed)

 #御籤 
    #「翠、おみくじ引かせて！」って言うとおみくじ引く
    if message.content == 'おみくじ' or message.content == '運勢':
        prob = random.random()
    
        if prob < 0.3:
            await message.channel.send('凶です……外出を控えることをオススメします(  ･᷄ὢ･᷅  )')
        
        elif prob < 0.65:
            await message.channel.send('吉です！何かいい事があるかもですね！')
        
        elif prob < 0.71:
            await message.channel.send('末吉……どれくらい運がいいんでしょうね？•́ω•̀)?')
        
        elif prob < 0.76:
            await message.channel.send('半吉は吉の半分、つまり運がいいのです！')
        
        elif prob < 0.80:
            await message.channel.send('小吉ですね！ちょっと優しくされるかも？')
        
        elif prob < 0.83:
            await message.channel.send('吉の中で1番当たっても微妙に感じられる……つまり末吉なのです( ´･ω･`)')
       
        elif prob <= 1.0:
            await message.channel.send('おめでとうございます！大吉ですよ！(๑>∀<๑)♥')   

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '09:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはようございます！9:00です！今日も一日頑張りましょう！')  
    elif now == '23:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おやすみなさい！23:00です！以降のメンションはお控え下さい。') 
#ループ処理実行
loop.start()

client.run(TOKEN)
