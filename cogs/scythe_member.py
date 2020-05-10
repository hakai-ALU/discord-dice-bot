import os
import r
from discord.ext import commands

class scythe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.name_bea = 0

    @commands.command(name='登録')
    async def touroku(self, ctx):
        conn = r.connect()
        k = conn.keys()
        cai = ctx.author.id
        for i in k:
            if i == cai:
                name_bea = 1
        if name_bea == 1:
            nb = conn.set(cai,"1")
            if nb == "True":
                await ctx.send("登録しました。\n登録特典で1Point付与しました。")   
            else:
                await ctx.send("登録に失敗しました。\nやり直して下さい。")
        else:
            await ctx.send("既に登録済みです。")

    @commands.command()
    async def delbet(self, ctx):
        conn = r.connect()
        ad = conn.flushdb()
        await ctx.send(ad)  
     
    @commands.command()
    async def set(self, ctx, what1, what2):
        conn = r.connect()
        q = conn.set(what1, what2)
        await ctx.send(q)

    @commands.command()
    async def get(self, ctx, what1):
        conn = r.connect()
        p = conn.get(what1)
        await ctx.send(p)

    @commands.command()
    async def sadd(self, ctx, what):
        conn = r.connect()
        q = conn.sadd("what2", what)
        await ctx.send(q)

    @commands.command()
    async def smembers(self, ctx):
        conn = r.connect()
        p = conn.smembers("what2")
        for w in p:
            await ctx.send(w)

    @commands.command()
    async def key(self, ctx):
        conn = r.connect()
        ak = conn.keys()
        for k in ak:
            await ctx.send(k)

    @commands.command()
    async def delete(self, ctx, what):
        conn = r.connect()
        d = conn.delete(what)
        await ctx.send(d)

    @commands.command()
    async def alldelete(self, ctx):
        conn = r.connect()
        ad = conn.flushdb()
        await ctx.send(ad)

def setup(bot):
    bot.add_cog(scythe(bot))
