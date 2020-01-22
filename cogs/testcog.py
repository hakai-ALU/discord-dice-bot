from discord.ext import commands # Bot Commands Frameworkのインポート

import discord

import random

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    async def what(self, ctx, what):
        await ctx.send(f'{what}とはなんですか？')
    
    # メインとなるroleコマンド
    @commands.group()
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command()
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command()
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command()
    async def create(self, ctx):
        guild = ctx.guild
        set_name = self.user.id
        await guild.create_role(name=set_name)
        await ctx.send('作成しました')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == 'こんにちは':
            await message.channel.send('こんにちは')
          
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
