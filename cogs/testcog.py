from discord.ext import commands # Bot Commands Frameworkのインポート

import discord

import asyncio

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        await ctx.send(f'{what}')

    #bans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def ban(self, ctx, member:discord.User=None, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("BAN対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        message = f"貴方は{ctx.guild.name}からBANされました。\n理由:{reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} をBANしました。")

    #bans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def kick(self, ctx, member:discord.User=None, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("KICK対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        message = f"貴方は{ctx.guild.name}からKICKされました。\n理由:{reason}"
        await member.send(message)
        await ctx.guild.kick(member, reason=reason)
        await ctx.channel.send(f"{member} をKICKしました。")

    # メインとなるroleコマンド
    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

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
    @role.command(aliases=['cr'])
    async def create(self, ctx, what):
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2)
        await ctx.send(f'作成しました。@' + set_name2)
        
    @commands.Cog.listener()
    @commands.has_permissions(manage_guild=True)
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == 'ログ削除して':
            await message.channel.purge()
            msg = await message.channel.send("削除しました。")
            await asyncio.sleep(15)
            await msg.delete()

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
