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
        await ctx.delete()
        if question == None:
            await ctx.send("質問を設定して下さい。")
            return
        else:
            poll_embed = discord.Embed(title=question, description=None)
        if answer1 != None:
            if answer2 == None:    
                await ctx.send("二つ以上の答えを設定して下さい。")
                return
            poll_embed.add_field(name='1⃣',value=answer1)
            poll_embed.add_field(name='2⃣',value=answer2) 
        if answer3 != None:
            poll_embed.add_field(name='3⃣',value=answer3)
        if answer4 != None:
            poll_embed.add_field(name='4⃣',value=answer4)
        if answer5 != None:
            poll_embed.add_field(name='5⃣',value=answer5)
        msg = await ctx.send(embed=poll_embed)
        if answer1 == None:
            await msg.add_reaction('⭕')
            await msg.add_reaction('❌')
        if answer2 != None:
            await msg.add_reaction('1⃣')
            await msg.add_reaction('2⃣') 
        if answer3 != None:
            await msg.add_reaction('3⃣')
        if answer4 != None:
            await msg.add_reaction('4⃣')
        if answer5 != None:
            await msg.add_reaction('5⃣')      

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(poll(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
