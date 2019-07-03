import discord 
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

client.run(TOKEN)
