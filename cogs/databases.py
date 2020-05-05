import os
import r
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bet(self, ctx, what):
        if ctx.author.id == 459936557432963103:
            conn = r.connect()
            bt = conn.sadd("bet", what)
            await ctx.send(bt)
            bts = conn.smembers("bet")
            await ctx.send("`" + str(bts) + "`")

    @commands.command()
    async def delbet(self, ctx):
        conn = r.connect()
        ad = conn.flushdb()
        await ctx.send(ad)  
     
    @commands.command()
    async def set(self, ctx, what1, what2):
        conn = r.connect()
        betatester = conn.smembers("bet")
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        q = conn.set(what1, what2)
        await ctx.send(q)

    @commands.command()
    async def get(self, ctx, what1):
        conn = r.connect()
        betatester = conn.smembers("bet")
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        p = conn.get(what1)
        await ctx.send(p)

    @commands.command()
    async def sadd(self, ctx, what):
        conn = r.connect()
        betatester = conn.smembers("bet")
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        q = conn.sadd("what2", what)
        await ctx.send(q)

    @commands.command()
    async def smembers(self, ctx):
        conn = r.connect()
        betatester = conn.smembers("bet")
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        p = conn.smembers("what2")
        for w in p:
            await ctx.send(w)

    @commands.command()
    async def key(self, ctx):
        conn = r.connect()
        betatester = conn.smembers("bet")
        await ctx.send(betatester)
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        ak = conn.keys()
        for k in ak:
            await ctx.send(k)

    @commands.command()
    async def delete(self, ctx, what):
        conn = r.connect()
        betatester = conn.smembers("bet")
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        d = conn.delete(what)
        await ctx.send(d)

    @commands.command()
    async def alldelete(self, ctx):
        conn = r.connect()
        betatester = conn.smembers("bet")
        if ctx.author.id in betatester:
            await ctx.send("True")
        else:
            await ctx.send("貴方はベータテスターではありません。")
            return
        ad = conn.flushdb()
        await ctx.send(ad)

def setup(bot):
    bot.add_cog(Example(bot))
