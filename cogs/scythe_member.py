import os
import r
from discord.ext import commands

class scythe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.namebea = 0

    @commands.command(name="登録")
    async def sighin(self, ctx):
        conn = r.connect()
        k = conn.keys()
        cai = ctx.author.id
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

def setup(bot):
    bot.add_cog(scythe(bot))
