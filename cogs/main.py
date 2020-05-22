from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
from func import diceroll

# コグとして用いるクラスを定義。
class main(commands.Cog):
    # mainクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith("dc"):
            # 入力された内容を受け取る
            say = message.content 

            # [dc ]部分を消し、AdBのdで区切ってリスト化する
            order = say.strip('dc ')
            cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
            dice = diceroll(cnt, mx) # 和を計算する関数(後述)
            await message.channel.send(dice[cnt])
            del dice[cnt]

            # さいころの目の総和の内訳を表示する
            await message.channel.send(dice)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(main(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
