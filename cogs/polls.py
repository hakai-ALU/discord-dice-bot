from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio

# コグとして用いるクラスを定義。
class poll(commands.Cog):
    # pollクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, question= None, answer1= None, answer2= None, answer3= None, answer4= None, answer5= None):  
        """質問5つまで"""
        if question == None:
            await ctx.send("質問を設定して下さい。")
            return
        else:
            poll_embed = discord.Embed(title=question, description=None)
        if answer1 != None:
            poll_embed.add_field(name=f'1⃣{answer1}',value="")
        if answer2 != None:
            poll_embed.add_field(name=f'2⃣{answer2}',value="")
        if answer3 != None:
            poll_embed.add_field(name=f'3⃣{answer3}',value="")
        if answer4 != None:
            poll_embed.add_field(name=f'4⃣{answer4}',value="")
        if answer5 != None:
            poll_embed.add_field(name=f'5⃣{answer5}',value="")
        await ctx.send(embed=poll_embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(poll(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
