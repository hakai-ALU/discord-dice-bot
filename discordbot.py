import discord
import os 

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/n」と発言したら「にゃーん」が返る処理
    if message.content == '/n':
        await message.channel.send('にゃーん')

client.run(TOKEN)
