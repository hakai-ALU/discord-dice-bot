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

    #if 'joined; Invited by DISBOARD' in message.content:
        if '(7 invites)' in message.content:
            role1 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role1)
        if '(14 invites)' in message.content:
            role2 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role2)
        if '(21 invites)' in message.content:
            role3 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role3)
        if '(28 invites)' in message.content:
            role4 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role4)
        if '(35 invites)' in message.content:
            role5 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role5)
        if '(42 invites)' in message.content:
            role6 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role6)
        if '(49 invites)' in message.content:
            role7 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role7)
        if '(56 invites)' in message.content:
            role8 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role8)
        if '(63 invites)' in message.content:
            role9 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role9)
        if '(70 invites)' in message.content:
            role10 = discord.utils.get(message.guild.roles, name='class SAXONY')
            await message.author.add_roles(role10)


client.run(TOKEN)

#ノア
#グローバルチャット
