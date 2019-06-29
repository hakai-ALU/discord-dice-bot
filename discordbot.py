import discord
import os 
import datetime
import random

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

date = datetime.datetime.now()
hour = date.hour+9
@client.event
async def on_ready():
    print('Hello World,対話botプログラム「Project-ririna-」、起動しました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
 # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
 #年月日
    if all(s in message.content for s in['何日？']):
        date = datetime.datetime.now()
        await message.channel.send(f'今日は{date.year}年{date.month}月{date.day}日です！')    
    if all(s in message.content for s in ['何時？']):
        date = datetime.datetime.now()
        await message.channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒だよ！')

@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "DM":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんどうしましたか？もし、質問・要望等ありましたら、以下のサバで言ってもらえると嬉しいです（ https://discord.gg/mCs822d ）")

client.run(TOKEN)

