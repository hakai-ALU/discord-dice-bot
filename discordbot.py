import discord 
import os
import asyncio

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#起動メッセージ
@client.event
async def on_ready():
    print("起動しました")

@client.event
async def on_message(message):
    if 'Bumpを確認しました' in message.content:
        await asyncio.sleep(1)
        channel_bot_test = [channel for channel in client.get_all_channels() if channel.name == 'noa-global-chat'][0]

    if 'Bumpを確認しました' in message.content:
        await asyncio.sleep(1)
        await message.channel.send('bumpを確認しました！2時間後お願いします！') 
        await asyncio.sleep(2*60*60)
        await message.channel.send('bumpチャンス！') 

    if message.author == message.guild.me:
        return

client.run(TOKEN)

#ノア
#グローバルチャット
#1
