from discord.ext import commands # Bot Commands Frameworkのインポート

import discord

import asyncio

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        await ctx.send(f'{what}')


    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        for i in range(5):
            await ctx.send(f'No.{i} Latency: {round(self.bot.latency * 1000)}ms')

    #gbans a user with a reason
    @commands.command()
    async def gban(self, ctx, user_id: int, reason =None):
        if ctx.author.id != great_owner_id:
            return
        member = self.bot.get_user(user_id)
        if reason == None:
            reason = "None"
        for g in self.bot.guilds:
            guildf = self.bot.get_guild(g.id)
            await guildf.ban(discord.Object(user_id), reason=reason)
            await ctx.channel.send(f"{g}からのBANが完了しました。")
            if g == None:
                await self.bot.logout()

    #gunbans a user with a reason
    @commands.command()
    async def gunban(self, ctx, user_id: int, reason =None):
        if ctx.author.id != great_owner_id:
            return
        member = self.bot.get_user(user_id)
        if reason == None:
            reason = "None"
        for g in self.bot.guilds:
            guildf = self.bot.get_guild(g.id)
            await guildf.unban(discord.Object(user_id), reason=reason)
            await ctx.channel.send(f"{g}からのUNBANが完了しました。")
            if g == None:
                await self.bot.logout()
        
    #bans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def ban(self, ctx, user_id: int, reason =None):
        member = self.bot.get_user(user_id)
        banlog = self.bot.get_channel(694044656501129317)
        if member == None or member == ctx.message.author:
            await ctx.channel.send("BAN対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        message = f"貴方は{ctx.guild.name}からBANされました。\n理由:{reason}"
        await ctx.guild.ban(discord.Object(user_id), reason=reason)
        await member.send(message)
        await ctx.channel.send(f"{member} をBANしました。")
        await banlog.send(f"BAN通知 \n 鯖名：{ctx.guild.name} \n user id：{user_id} \n 理由：{reason}")

    #unbans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def unban(self, ctx, user_id: int, reason =None):
        member = self.bot.get_user(user_id)
        banlog = self.bot.get_channel(694044656501129317)
        if member == None or member == ctx.message.author:
            await ctx.channel.send("UNBAN対象が正しくありません")
            return
        if reason == None:
            reason = "無し"
        message = f"貴方は{ctx.guild.name}のBANが解除されました。\n理由:{reason}"
        await ctx.guild.unban(user_id, reason=reason)
        await member.send(message)
        await ctx.channel.send(f"{member} をUNBANしました。")
        await banlog.send(f"UNBAN通知 \n 鯖名：{ctx.guild.name} \n user id：{user_id} \n 理由：{reason}")

    #kick a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def kick(self, ctx, member:discord.User=None, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("KICK対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        message = f"貴方は{ctx.guild.name}からKICKされました。\n理由:{reason}"
        await ctx.guild.kick(member, reason=reason)
        await member.send(message)
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
        if message.author.id != great_owner_id:
            return
        if message.content == 'ログ削除して':
            await message.channel.purge()
            msg = await message.channel.send("削除しました。")
            await asyncio.sleep(15)
            await msg.delete()

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
