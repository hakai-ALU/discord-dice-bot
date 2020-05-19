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
        
def setup(bot):
    bot.add_cog(TRPG(bot))
