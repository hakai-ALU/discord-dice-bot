import discord
import os 
import datetime

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

date = datetime.datetime.today()

@client.event
async def on_ready():
    print('Hello World,対話botプログラム「Project-ririna-」、起動しました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content.startswith('何日？'):
        await message.channel.send('今日は'+str(date.year)+'年'+str(date.month)+'月'+str(date.day)+'日です！')	
    if message.content.startswith('時間？'):
        await message.channel.send('今は'+str(date.hour)+'時'+str(date.minute)+'分'+str(date.second)+'秒です！')	        
     
client.run(TOKEN)
