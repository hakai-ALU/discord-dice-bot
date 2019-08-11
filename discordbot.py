import discord 
import os

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return

    voice = await client.join_voice_channel(client.get_channel("577830004231110677"))
    if message.content == ("lecture"):
        player = await voice.create_ytdl_player('https://youtu.be/mN7u3h-BZjY')
        player.start()

client.run(TOKEN)
