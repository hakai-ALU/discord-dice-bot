from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio

# コグとして用いるクラスを定義。
class Template(commands.Cog):
    # Templateクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Template(bot)) 
# mainにBotを渡してインスタンス化し、Botにコグとして登録する。
