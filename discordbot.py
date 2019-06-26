import discord
import os 
from datetime import datetime

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

date = datetime.datetime.now()

@client.event
async def on_ready():
    print('Hello World,対話botプログラム「Project-ririna-」、起動しました')

# メッセージ受信時に動作する処理
@client.event
   async def on_message(message):
 # メッセージ送信者がBotだった場合は無視する
    　　if message.author.bot:
        　　return
　　　　#!timeとサーバのチャット欄に打てば現在時刻を教えてくれる
       if message.content.startswith('何日？'):
           replay = datetime.now().strftime("%Y年%m月%d日 %H時:%M分:%S秒")       
           await client.send_message(message.channel, replay) 


client.run(TOKEN)

