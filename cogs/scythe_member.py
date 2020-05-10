import os
import r
from discord.ext import commands
import discord

class scythe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.namebea = 0

    @commands.command(name="登録")
    async def sighin(self, ctx):
        """ポイント制度登録"""
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
        conn = r.connect()
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

def setup(bot):
    bot.add_cog(scythe(bot))
