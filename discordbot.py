import discord 
import os
from discord.ext import tasks
from datetime import datetime

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 587658526013390859 #チャンネルID
CHANNEL_ID2 = 603203288883789831
# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    print('Hello World,リマインドbotプログラム「project-remain」、起動しました')
    channel = client.get_channel(CHANNEL_ID2)
    await channel.send('BOT再起動しました')
          
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
