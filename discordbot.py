import discord 
import os

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#起動メッセージ
@client.event
async def on_ready():
    client.global_list = []
    for guild in client.guilds:
        tmp = discord.utils.get(guild.text_channels,name="noa-global-chat")
        if tmp: client.global_list.append(tmp)
    print("起動しました")

@client.event
async def on_message(message):

    if message.author == message.guild.me:
        return

    if message.webhook_id:
        return

    global_tmp = [w for w in await message.channel.webhooks() if w in client.global_list]

    if message.content == "!noa-global":
        if message.author.guild_permissions.administrator:
            if global_tmp:
                await message.channel.send("既に登録されています。")
                return

            new_w = await message.channel.create_webhook(name="global")
            client.global_list.append(new_w)
            await message.channel.send("グローバルチャットのチャンネルに登録しました。")
            return
       
    for webhook in client.global_list:
        if message.channel != webhook.channel:
            await webhook.send(content=message.content,username=message.author.name,avatar_url=message.author.avatar_url)


client.run(TOKEN)

#ノア
#グローバルチャット
#1
