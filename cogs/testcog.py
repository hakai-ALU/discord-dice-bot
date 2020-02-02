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
