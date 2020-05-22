from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio

# コグとして用いるクラスを定義。
class main(commands.Cog):
    # mainクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['dc'])
    async def dice(self, ctx, what=none):
        """dc AdB"""

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(main(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
