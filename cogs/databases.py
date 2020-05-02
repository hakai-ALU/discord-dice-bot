import os
import psycopg2
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        DATABASE_URL = os.getenv("DATABASE_URL")
        self.db = psycopg2.connect(DATABASE_URL, sslmode="require")
        self.db_cursor = self.db.cursor()
        self.db_cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS bot;
        CREATE TABLE IF NOT EXISTS bot.users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            discriminator TEXT NOT NULL
        );
        """)

        @commands.command(name="whoami")
        async def whoami(self, ctx):
            self.db_cursor.exe("SELECT * FROM bot.users WHERE id=%s", (ctx.author.id,))
            response = self.db_cursor.fetchone()
            if not reponse:
                self.db_cursor.execute("INSERT INTO bot.users VALUES (%s,%s,%s)",
                    (str(ctx.author.id), ctx.author.name, ctx.author.discriminator,))
                self.db.commit()

            uid, name, discriminator = response
            await ctx.send("<@{}>, you are {}#{}.".format(uid, name, discriminator))

def setup(bot):
    bot.add_cog(Example(bot))
