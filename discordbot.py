import discord 
import os
import asyncio
from discord.ext import tasks
from datetime import datetime

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
        await message.channel.send('bumpを確認しました！2時間後お願いします！') 
        await asyncio.sleep(2*60*60)
        await message.channel.send('<@&650506130325372950> bumpチャンス！') 

    if message.content == 'ステータス':
        if message.author.guild_permissions.administrator:
            await message.channel.send(f'サーバー名：{message.guild.name}')
            await message.channel.send(f'現オーナー名：{message.guild.owner}')
            member_count_server = len(message.guild.members) 
            await message.channel.send(f'今のサーバー人数(BOT含む)：{member_count_server}人')
            await message.channel.send(f'総チャンネル数：{len(message.guild.channels)}個')
            await message.channel.send(f'テキストチャンネル数：{len(message.guild.text_channels)}個')
            await message.channel.send(f'ボイスチャンネル数：{len(message.guild.voice_channels)}個')
            embed = discord.Embed(title="サーバーアイコン")
            embed.set_image(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
          
        if not message.author.guild_permissions.administrator:
            await message.channel.send('貴方は管理者権限がありません。 \n You do not have admin roles !!')
              
client.run(TOKEN)

#ノア
#グローバルチャット
