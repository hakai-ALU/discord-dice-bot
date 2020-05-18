from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
from func import diceroll

class TRPG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("dc"):
            # 入力された内容を受け取る
            say = message.content 

            # [rtdc ]部分を消し、AdBのdで区切ってリスト化する
            order = say.strip('dc ')
            cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
            dice = diceroll(cnt, mx) # 和を計算する関数(後述)
            await message.channel.send(dice[cnt])
            del dice[cnt]

            # さいころの目の総和の内訳を表示する
            await message.channel.send(dice)

def setup(bot):
    bot.add_cog(TRPG(bot))
