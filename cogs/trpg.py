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

    @commands.command(name='TRPG値')
    async def trpg(self, ctx):
        """TRPG探索者値"""
        embed = discord.Embed(title=f"**{ctx.author.name}さんの能力値**", description=None,color=0x2ECC69)
        embed.set_thumbnail(url=ctx.author.avatar_url)

        str1=random.randint(3,18)
        embed.add_field(name="**STR(筋力)**", value=f"`{str1}`")

        con1=random.randint(3,18)
        embed.add_field(name="**CON(体力)**", value=f"`{con1}`")

        pow1=random.randint(3,18)
        embed.add_field(name="**POW(精神力)**", value=f"`{pow1}`")

        dex1=random.randint(3,18)
        embed.add_field(name="**DEX(敏捷)**", value=f"`{dex1}`")

        app1=random.randint(3,18)
        embed.add_field(name="**APP(容姿)**", value=f"`{app1}`")

        siz1=random.randint(2,12)
        siz1+=6
        embed.add_field(name="**SIZ(体格)**", value=f"`{siz1}`")

        int1=random.randint(2,12)
        int1+=6
        embed.add_field(name="**INT(知性)**", value=f"`{int1}`")

        edu1=random.randint(3,18)
        edu1+=3
        embed.add_field(name="**EDU(教養)**", value=f"`{edu1}`")

        sun1=pow1*5
        embed.add_field(name="**SAN(正気度)**", value=f"`{sun1}`")

        await ctx.send(embed=embed)

        embed2 = discord.Embed(title=f"**{ctx.author.name}さんの能力値ロール**", description=None,color=0x2ECC69)
        embed2.set_thumbnail(url=ctx.author.avatar_url)

        ida1=int1*5
        embed2.add_field(name="**アイデア**", value=f"`{ida1}`")

        rac1=pow1*5
        embed2.add_field(name="**幸運", value=f"`{rac1}`")

        lun1=edu1*5
        embed2.add_field(name="**知識**", value=f"`{lun1}`")

        dab1=str1+siz1
        if dab1 <= 12:
            embed2.add_field(name="**ダメージボーナス**", value="`1D6`")
        elif 12 < dab1 < 17:
            embed2.add_field(name="**ダメージボーナス**", value="`1D4`")
        elif 16 < dab1 < 25:
            embed2.add_field(name="**ダメージボーナス**", value="`0`")
        elif 24 < dab1 < 33:
            embed2.add_field(name="**ダメージボーナス**", value="`1D4`")
        elif 32 < dab1 < 41:
            embed2.add_field(name="**ダメージボーナス**", value="`1D6`")
        elif 40 < dab1 < 57:
            embed2.add_field(name="**ダメージボーナス**", value="`2D6`")
        elif 56 < dab1 < 73:
            embed2.add_field(name="**ダメージボーナス**", value="`3D6`")
        elif 72 < dab1 < 90:
            embed2.add_field(name="**ダメージボーナス**", value="`4D6`")

        tai1=con1+siz1
        tai1=tai1//2
        embed2.add_field(name="**耐久力(少数切捨)**", value=f"`{tai1}`")

        mp1=pow1
        embed2.add_field(name="**MP**", value=f"`{mp1}`")

        await ctx.send(embed=embed2)

        embed3 = discord.Embed(title=f"**その他**", description=None,color=0x2ECC69)
        embed3.set_thumbnail(url=ctx.author.avatar_url)

        wrp1=edu1*20
        embed3.add_field(name="**割り振りポイント**", value=f"`{wrp1}`")

        embed3.add_field(name="**参考サイト**", value="[クトゥルフ神話TRPG初心者用Wiki](<https://seesaawiki.jp/cthulhu/d/%C3%B5%BA%F7%BC%D4%A4%CE%BA%EE%C0%AE%CB%A1>)")

        await ctx.send(embed=embed3)
        
def setup(bot):
    bot.add_cog(TRPG(bot))
