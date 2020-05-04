import os
from rdb import con
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def set(self, ctx, what1, what2):
        conn = rdb.connect()
        q = conn.set(what1, what2)
        await ctx.send(q)

    @commands.command()
    async def get(self, ctx, what1):
        conn = rdb.connect()
        p = conn.get(what1)
        await ctx.send(p)

def setup(bot):
    bot.add_cog(Example(bot))
