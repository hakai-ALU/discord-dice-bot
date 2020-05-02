import os
import sqlite3
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        DATABASE_URL = os.getenv("DATABASE_URL")
        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        c.execute("""
        CREATE SCHEMA IF NOT EXISTS bot;
        CREATE TABLE IF NOT EXISTS bot.users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            discriminator TEXT NOT NULL
        );
        """)

        @commands.command(name="whoami")
        async def whoami(self, ctx):
            c.exe("SELECT * FROM bot.users WHERE id=%s", (ctx.author.id,))
            response = c.fetchone()
            if not reponse:
                c.execute("INSERT INTO bot.users VALUES (%s,%s,%s)",
                    (str(ctx.author.id), ctx.author.name, ctx.author.discriminator,))
                conn.commit()

            uid, name, discriminator = response
            await ctx.send("<@{}>, you are {}#{}.".format(uid, name, discriminator))

def setup(bot):
    bot.add_cog(Example(bot))
