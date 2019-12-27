import discord 
import os
import asyncio
from discord.ext import tasks
from datetime import datetime

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 648435960077615127

# 接続に必要なオブジェクトを生成
client = discord.Client()

#起動メッセージ
@client.event
async def on_ready():
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('----------------')
    print('Hello World,リマインドbotプログラム「project-RRN」、起動しました')
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f'名前:{client.user.name}')  # ボットの名前
    await channel.send(f'ID:{client.user.id}')  # ボットのID
    await channel.send(f'Discord ver:{discord.__version__}')  # discord.pyのバージョン
    await channel.send('----------------')
    await channel.send('状態：BOT再起動しました。')   
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(name='ギルド専属ナビ'))
    

@client.event
async def on_message(message):
    
    if 'Bumpを確認しました' in message.content:
        await message.channel.send('bumpを確認しました！2時間後お願いします！') 
        await asyncio.sleep(2*60*60)
        await message.channel.send('<@&650506130325372950> bumpチャンス！') 

    if message.content == 'ステータス':
        if message.author.guild_permissions.administrator:
            await message.channel.send(f'サーバー名：{message.guild.name}')
            await asyncio.sleep(0.1)
            await message.channel.send(f'現オーナー名：{message.guild.owner}')
            await asyncio.sleep(0.1)
            guild = message.guild
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            await message.channel.send(f'総人数：{all_count}人')
            await asyncio.sleep(0.1)
            await message.channel.send(f'ユーザ数：{member_count}')
            await asyncio.sleep(0.1)
            await message.channel.send(f'BOT数：{bot_count}')
            await asyncio.sleep(0.1) 
            await message.channel.send(f'総チャンネル数：{len(message.guild.channels)}個')
            await asyncio.sleep(0.1)
            await message.channel.send(f'テキストチャンネル数：{len(message.guild.text_channels)}個')
            await asyncio.sleep(0.1)
            await message.channel.send(f'ボイスチャンネル数：{len(message.guild.voice_channels)}個')
            await asyncio.sleep(0.1)
            embed = discord.Embed(title="サーバーアイコン")
            embed.set_image(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
        if not message.author.guild_permissions.administrator:
            await message.channel.send('貴方は管理者権限がありません。 \n You do not have admin roles !!')

    if message.content == 'ステータスE':
        if message.author.guild_permissions.administrator:
            embed = discord.Embed(title="この鯖のステータス",description="Embed式")
            embed.add_field(name="サーバー名",value=f'{message.guild.name}',inline=False)
            embed.add_field(name="現オーナー名",value=f'{message.guild.owner}',inline=False)
            guild = message.guild
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            embed.add_field(name="総人数",value=f'{all_count}',inline=False)
            embed.add_field(name="ユーザ数",value=f'{member_count}',inline=False)
            embed.add_field(name="BOT数",value=f'{bot_count}',inline=False)
            embed.add_field(name="総チャンネル数",value=f'{len(message.guild.channels)}個',inline=False)
            embed.add_field(name="テキストチャンネル数",value=f'{len(message.guild.text_channels)}個',inline=False)
            embed.add_field(name="ボイスチャンネル数",value=f'{len(message.guild.voice_channels)}個',inline=False)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)

        if not message.author.guild_permissions.administrator:
            await message.channel.send('貴方は管理者権限がありません。 \n You do not have admin roles !!')

        #年月日
    if message.content.startswith('何日？') or message.content == '何日?':
        date = datetime.now()
        await message.channel.send(f'今日は{date.year}年{date.month}月{date.day}日です！')    
    if message.content.startswith('何時？') or message.content == '何時?':
        date = datetime.now()
        await message.channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')

              
client.run(TOKEN)

#ノア
#グローバルチャット
