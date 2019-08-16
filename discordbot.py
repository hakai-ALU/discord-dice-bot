import discord 
import os

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#チャンネルID
CHANNEL_ID = 610388405926494211

ownerid = 459936557432963103

user_id = memmber.id

#発言した奴のID取得
@client.event
async def on_message(message):
    if not message.author.bot: 
        await client.get_channel(CHANNEL_ID).send(message.author.id)  

#入ってきた奴のID取得
@client.event
async def on_member_join(member):
    await client.get_channel(CHANNEL_ID).send(member.id)            

#出て行った奴のID取得
@client.event
async def on_member_remove(member):
    await client.get_channel(CHANNEL_ID).send(member.id)            
    
#発言した奴のID取得
@client.event
async def on_message(message):
    if message.author.bot: 
        return
    
client.run(TOKEN)
