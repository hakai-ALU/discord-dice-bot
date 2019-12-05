import discord 
import os
import asyncio
from discord.ext import tasks
from datetime import datetime
import re

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

async def message_count(channel):
    """チャンネル名にあるメッセージ数を1増やす"""
    matched = re.match(r"(.+)（(\d+)）",channel.name)

    if matched:
        #もし、メッセージのカウントが既に行われていたら
        base_name = matched.groups()[0] # 元のチャンネル名
        count = int(matched.groups()[1]) # メッセージ数
        await channel.edit(name=f"{base_name}（{count+1}）")
        return

    count = 0
    async for message in channel.history(limit=None):
        if not message.author.bot:
            # 人間が投稿していたらカウントを1増やす
            count += 1 

    await channel.edit(name=f"{channel.name}（{count}）")

#起動メッセージ
@client.event
async def on_ready():
    print("起動しました")

@client.event
async def on_message(message):
    
    if 'Bumpを確認しました' in message.content:
        await message.channel.send('bumpを確認しました！2時間後お願いします！') 
        await asyncio.sleep(2*60*60)
        await message.channel.send('<@&650506130325372950> bumpチャンス！') 

    if message.author == message.guild.me:
        return

client.run(TOKEN)

#ノア
#グローバルチャット
