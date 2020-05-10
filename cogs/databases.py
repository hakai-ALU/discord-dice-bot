import os
import r
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.ahomin = 459936557432963103

    @commands.command()
    async def set(self, ctx, what1, what2):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        q = conn.set(what1, what2)
        await ctx.send(q)

    @commands.command()
    async def get(self, ctx, what1):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        p = conn.get(what1)
        await ctx.send(p)

    @commands.command()
    async def sadd(self, ctx, what1, what2):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        q = conn.sadd(what1, what2)
        await ctx.send(q)

    @commands.command()
    async def smembers(self, ctx, whst):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        p = conn.smembers(f'{what}')
        for w in p:
            await ctx.send(w)

    @commands.command()
    async def key(self, ctx):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        ak = conn.keys()
        for k in ak:
            await ctx.send(f"`{k}`")

    @commands.command()
    async def delete(self, ctx, what):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        d = conn.delete(what)
        await ctx.send(d)

    @commands.command()
    async def alldelete(self, ctx):
        if ctx.author.id != self.ahomin:
            return await ctx.send("貴方は使えません")
        conn = r.connect()
        ad = conn.flushdb()
        await ctx.send(ad)

def setup(bot):
    bot.add_cog(Example(bot))
