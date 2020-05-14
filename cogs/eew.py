from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import json
import requests

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class eew(commands.Cog):
    # testクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gban(self, ctx):
        """Test1(開発者用)"""
        if ctx.author.id != great_owner_id:
            return

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(eew(bot))
