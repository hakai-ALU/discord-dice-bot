import os
import r
from discord.ext import commands
import discord

class scythe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.namebea = 0
        self.givepoint = 0

    @commands.command(name="登録")
    async def sighin(self, ctx):
        """ポイント制度登録"""
        self.namebea = 0
        conn = r.connect()
        k = conn.keys()
        cai = str(ctx.author.id)
        for i in k:
            if i == cai:
                self.namebea += 1
        if self.namebea == 0:
            nb = conn.set(cai,"1")
            if nb == True:
                await ctx.send("登録しました。\n登録特典で1Point付与しました。")   
            else:
                await ctx.send("登録に失敗しました。\nやり直して下さい。")
        else:
            await ctx.send("既に登録済みです。")

    @commands.command(name="ポイント確認")
    async def get_point(self, ctx, user_id:int= None):
        """ポイントの確認"""
        conn=r.connect()
        ci = str(ctx.author.id)
        gu = self.bot.get_user(user_id)
        ui = str(user_id)
        if user_id == None:
            embed = discord.Embed(title=f"**{ctx.author.name}さんの情報**", description=None)
            up = conn.get(ci)
            embed.add_field(name="現在ポイント", value=f"`{up}p`")
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title=f"**{gu.name}さんの情報**", description=None)
            up = conn.get(ui)
            embed.add_field(name="現在ポイント", value=f"`{up}p`")
            await ctx.send(embed=embed)
            return

    @commands.command(name="P制御")
    async def give_point(self, ctx, user_id:int=None, point:int=None):
        if user_id == None:
            return await ctx.send("ユーザーIDを設定して下さい。")
        if point == None:
            return await ctx.send("付与ポイントを設定して下さい。")
        self.givepoint = 0
        c = str(ctx.author.id)
        conn = r.connect()
        sm = conn.smembers('adomin')
        for ad in sm:
            if ad == c:
                self.givepoint += 1
        if self.givepoint == 0:
            return await ctx.send("貴方は操作できません。")
        un = self.bot.get_user(user_id)
        ui = str(user_id)
        up = conn.get(ui)
        up = int(up) + point
        us = conn.set(ui,up)
        if us == True:
            return await ctx.send(f"{un.name}さんに`{point}`P付与しました。")
        else:
            return await ctx.send("付与に失敗しました。\n最初からやり直して下さい。")

def setup(bot):
    bot.add_cog(scythe(bot))
