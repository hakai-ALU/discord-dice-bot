from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random

class TRPG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(TRPG(bot))
