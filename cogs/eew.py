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
        r = requests.get('http://svir.jp/eew/data.json')
        eew = r.json()
        embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
        embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
        embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
        embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
        embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
        embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
        await ctx.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(eew(bot))