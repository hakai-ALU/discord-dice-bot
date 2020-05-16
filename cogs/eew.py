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
        """地震情報(最新)"""
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
    async def eewop1(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        #Head
        embed=discord.Embed(title="**API識別タイトル、「緊急地震速報（予報）」で固定**", description=eew['Head']['Title'])
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Head']['DateTime'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Head']['EditorialOffice'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Head']['PublishingOffice'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Head']['EventID'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」はキャンセル報、「訓練」は訓練配信、「訓練取消」は訓練をキャンセル、「試験」は試験配信**", value=eew['Head']['Status'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Head']['Serial'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Head']['Version'], inline=False)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def eewop2(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        #body       
        embed=discord.Embed(title="**地震発生時刻**", description=eew['Body']['Earthquake']['OriginTime'])
        embed.add_field(name="**震央地名**", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False) 
        embed.add_field(name="**震央地名コード**", value=eew['Body']['Earthquake']['Hypocenter']['Code'], inline=False)
        embed.add_field(name="**震源位置の緯度**", value=eew['Body']['Earthquake']['Hypocenter']['Lat'], inline=False)
        embed.add_field(name="**震源位置の経度**", value=eew['Body']['Earthquake']['Hypocenter']['Lot'], inline=False)
        embed.add_field(name="**震源の深さ**", value=eew['Body']['Earthquake']['Hypocenter']['Depth'], inline=False)
        embed.add_field(name="**震源の陸海識別**", value=eew['Body']['Earthquake']['Hypocenter']['LandOrSea'], inline=False)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def eewop3(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        embed=discord.Embed(title="**震央の確からしさ0:不明1:P波/S波レベル越え、またはIPF法（1点）、または仮定震源要素の場合2:IPF法（2点）3:IPF法（3/4点）4:IPF法（5点以上）5:防災科研システム（4点以下、または精度情報なし）〈防災科研Hi-netデータ〉6:防災科研システム（5点以上）〈防災科研Hi-netデータ〉7:EPOS（海域〈観測網外〉）8:EPOS（陸域〈観測網内〉）9:予備**", description=eew['Body']['Earthquake']['Accuracy']['Epicenter[0]'])
        embed.add_field(name="**震源の確からしさ（気象庁内部システムで使用するため予告なく変わる場合がある）0:不明1:P波/S波レベル越え、またはIPF法（1点）、または仮定震源要素の場合2:IPF法（2点）3:IPF法（3/4点）4:IPF法（5点以上）5-8:予備9:従来法（IPF法を含む）の最終相当。推定震源・マグニチュードはこれ以降変化しない（ただしPLUM法により予想震度が今後変化する可能性はある）**", value=eew['Body']['Earthquake']['Accuracy']['Epicenter[1]'], inline=False)
        embed.add_field(name="**深さの確からしさ0:不明1:P波/S波レベル越え、またはIPF法（1点）、または仮定震源要素の場合2:IPF法（2点）3:IPF法（3/4点）4:IPF法（5点以上）5:防災科研システム（4点以下、または精度情報なし）〈防災科研Hi-netデータ〉6:防災科研システム（5点以上）〈防災科研Hi-netデータ〉7:EPOS（海域〈観測網外〉）8:EPOS（陸域〈観測網内〉）9:予備**", value=eew['Body']['Earthquake']['Accuracy']['Depth'], inline=False)
        embed.add_field(name="**マグニチュードの確からしさ0:不明1:未定義2:防災科研システム〈防災科研データ〉3:全点P相4:P相/全相混在5:全点全相6:EPOS7:未定義8:P波/S波レベル越え、または仮定震源要素の場合9:予備**", value=eew['Body']['Earthquake']['Accuracy']['MagnitudeCalculation'], inline=False) 
        embed.add_field(name="**マグニチュード計算使用観測点数（気象庁内部システムで使用するため予告なく変わる場合がある）0:不明1:P波/S波レベル越え、1点、または仮定震源要素の場合2:2点3:3点4:4点5:5点以上6-9:予備**", value=eew['Body']['Earthquake']['Accuracy']['NumberOfMagnitudeCalculation'], inline=False)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def eewop4(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        embed=discord.Embed(title="**マグニチュード不明時、「/./」となる**", description=eew['Body']['Earthquake']['Magnitude'], inline=False)
        embed.add_field(name="**最大予測震度1:震度12:震度23:震度34:震度45-:震度5弱5+:震度5強6-:震度6弱6+:震度6強7:震度7不明:不明時**", value=eew['Body']['Intensity']['MaxInt'], inline=False)
        embed.add_field(name="**テキストの予測最大震度**", value=eew['Body']['Intensity']['TextInt'], inline=False)
        embed.add_field(name="**最大予測震度の下限1:震度12:震度23:震度34:震度45-:震度5弱5+:震度5強6-:震度6弱6+:震度6強7:震度7不明:不明時**", value=eew['Body']['Intensity']['ForecastInt']['From'], inline=False)
        embed.add_field(name="**最大予測震度の上限1:震度12:震度23:震度34:震度45-:震度5弱5+:震度5強6-:震度6弱6+:震度6強7:震度7over:～程度以上不明:不明時**", value=eew['Body']['Intensity']['ForecastInt']['To'], inline=False)
        embed.add_field(name="**最大予測震度変化0:ほとんど変化なし1:最大予測震度が1.0以上大きくなった2:最大予測震度が1.0以上小さくなった3-9:未定義**", value=eew['Body']['Intensity']['MaxIntChange'], inline=False)
        embed.add_field(name="**最大予測震度変化の理由0:変化なし1:主としてMが変化したため（1.0以上）2:主として震央位置が変化したため（10㎞以上）3:M及び震央位置が変化したため（1と2の複合条件）4:震源の深さが変化したため（上記のいずれにも当てはまらず、30㎞以上変化）5-8:未定義9:PLUM法による予想により変化したため**", value=eew['Body']['Intensity']['MaxIntChangeReason'], inline=False)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def eewop5(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        #Head 
        embed=discord.Embed(title="**一次細分化地域名**", description=eew['Body']['Intensity']['Areas[]']['Name'], inline=False) 
        embed.add_field(name="**一次細分化地域コード**", value=eew['Body']['Intensity']['Areas[]']['Code'], inline=False)
        embed.add_field(name="**予報カテゴリー名の文字列表現「緊急地震速報（予報）」、「緊急地震速報（警報）」を記載。**", value=eew['Body']['Intensity']['Areas[]']['Kind']['Name'], inline=False)
        embed.add_field(name="**予報カテゴリー名のコード表現1桁目0:予報1:警報2桁目0:主要動未到達1:既に主要動到達と推測9:PLUM法での予測**", value=eew['Body']['Intensity']['Areas[]']['Kind']['Code'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Body']['Intensity']['Areas[]']['a'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Intensity']['Areas[]']['a'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Intensity']['Areas[]']['a'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Body']['Earthquake'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        
        await ctx.send(embed=embed)

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
