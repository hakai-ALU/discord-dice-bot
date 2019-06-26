import discord
import os 
import datetime

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
        if all(s in message.content for s in['何日？']):
            date = datetime.datetime.now()
            await message.channel.send(f'今日は{date.year}年{date.month}月{date.day}日です！')    
        if all(s in message.content for s in ['何時？']):
            date = datetime.datetime.now()
            await message.channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')

client.run(TOKEN)

