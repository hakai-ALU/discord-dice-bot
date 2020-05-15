from discord.ext import commands, tasks # Bot Commands Frameworkのインポート
import discord
import asyncio
import json
import urllib.request

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class eew(commands.Cog):
    # testクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        self.code = 0
        self.loop.start()

    def cog_unload(self, bot):
        self.loop.cancel() 

    @commands.command()
    async def eew(self, ctx):
        """Test1(開発者用)"""
        if ctx.author.id != great_owner_id:
            return
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
        embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
        embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
        embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
        embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
        embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def eewop(self, ctx):
        """Test2(開発者用)"""
        if ctx.author.id != great_owner_id:
            return
        await ctx.send(self.code)

    @tasks.loop(seconds=5)
    async def loop(self):
        channels=self.bot.get_all_channels()
        chw=[ch for ch in channels if ch.name == "eew"]
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        eew_code = eew['Head']['EventID']
        if eew_code != self.code:
            embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
            embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
            embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
            embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
            embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
            embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
            for chj in chw:   
                await chj.send(embed=embed)
            self.code = eew_code
    

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(eew(bot))
