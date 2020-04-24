from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio

# コグとして用いるクラスを定義。
class poll(commands.Cog):
    # pollクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, what1: int=None, what2: int=None, what3: int=None, what4: int=None, what3: int=None):  
        """質問5つまで"""

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(poll(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
