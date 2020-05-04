import os
from rdb import connect
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def set(self, ctx, what1, what2):
        conn = connect.connect()
        conn.set(what1, what2)

    @commands.command()
    async def get(self, ctx, what1):
        conn = connect.connect()
        p = conn.get(what1)
        await ctx.send(p)

def setup(bot):
    bot.add_cog(Example(bot))
