from discord.ext import commands # Bot Commands Frameworkのインポート

import discord

import random

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        await ctx.send(f'{what}')

    @commands.command(aliases=["計算問題", "計算クイズ"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def keisan_quiz(ctx):
        n1 = random.randint(0,300)
        n2 = random.randint(0,300)
        answer = n1+n2

        await ctx.send(ctx.message.author.mention + " >> " + str(n1) + "+" + str(n2) + " = ?")

        def answercheck(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()

        try:
            waitresp = await client.wait_for('message', timeout=30, check=answercheck)
        except asyncio.TimeoutError:
            await ctx.send(ctx.message.author.mention + " >> 時間切れです。正解は " + str(answer))
        else:
            if waitresp.content == str(answer):
                await ctx.send(ctx.message.author.mention + " >> 正解です！お見事！")
            else:
                await ctx.send(ctx.message.author.mention + " >> 不正解です。正解は " + str(answer))

    @keisan_quiz.error
    async def keisan_quiz_error(ctx, error):
        if isinstance(error, CommandOnCooldown):
            await ctx.send(ctx.message.author.mention + " >> 計算クイズはまだプレイできません(クールダウン中)")

    @commands.command()
    async def test(self, ctx, arg1, arg2): 
        await ctx.send(f'{arg1},{arg2}')
    
    # メインとなるroleコマンド
    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['cr'])
    async def create(self, ctx):
        guild = ctx.guild
        set1 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set2 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set3 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set4 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set_name = set1 + set2 + set3 + set4
        await guild.create_role(name=set_name)
        await ctx.send(f'作成しました。@' + set_name)
        
    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['ad'])
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send('付与しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command(aliases=['rm'])
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send('剥奪しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['cr2'])
    async def create2(self, ctx, what):
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2)
        await ctx.send(f'作成しました。@' + set_name2)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == '..i in':
            await message.channel.send('..in')

        if message.author.bot:
            return

        if message.content == 'こんにちは':
            await message.channel.send('こんにちは')

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
