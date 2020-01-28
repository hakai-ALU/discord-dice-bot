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

    @commands.command(aliases=['p'])
    async def poll(self, ctx, what1, what2, what3):
        await ctx.send(f'1.{what1}2.{what2}3.{what3}')

    @commands.group(aliases=['act'])
    @commands.has_permissions(manage_roles=True)
    async def activity(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # activityコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @activity.command()
    async def set(self, ctx, what):   
        await ctx.change_presence(activity=discord.Game(name=f'{what}'))
    
    # activityコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @activity.command()
    async def del(self, ctx):   
        await ctx.change_presence(activity=None)
    
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
        role2 = discord.Role(name=set_name2)
        await member.add_roles(role2)
        await ctx.send('付与しました。')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == 'こんにちは':
            await message.channel.send('こんにちは')

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
