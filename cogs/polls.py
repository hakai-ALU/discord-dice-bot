from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio

# コグとして用いるクラスを定義。
class poll(commands.Cog):
    # pollクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, question: int=None, answer1: int=None, answer2: int=None, answer3: int=None, answer4: int=None, answer5: int=None):  
        """質問5つまで"""
        if question == None:
            await ctx.send("質問を設定して下さい。")
            return
        else:
            poll_embed = discord.Embed(title=f'{question}', description=None)
        if answer1 != None:
            poll_embed.add_field(name=f'{answer1}',value=None)
        if answer2 != None:
            poll_embed.add_field(name=f'{answer2}',value=None)
        if answer3 != None:
            poll_embed.add_field(name=f'{answer3}',value=None)
        if answer4 != None:
            poll_embed.add_field(name=f'{answer4}',value=None)
        if answer5 != None:
            poll_embed.add_field(name=f'{answer5}',value=None)
        await ctx.send(embed=poll_embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(poll(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
