from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103
stopcodes = 0

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    global stopcodes

    @commands.command(aliases=['sc'])
    async def stopcode(self, ctx, stop_code: int=None):
        if stop_code == None:
            SCP = stopcodes
            await ctx.send(f'Stop Codeが指定されていません。\n`Stop Code={SCP}`')
            return
        stopcodes = stop_code
        await ctx.send(f'Stop Codeを設定しました。\n`Stop Code={stop_code}`')

    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        await ctx.send(f'{what}')

    @commands.command(aliases=['sinfo'])
    async def serverinfo(self, ctx, server_id: int=None):
        if server_id == None:
            embed = discord.Embed(title="鯖ステータス",description=f"Ping:`{self.bot.ws.latency * 1000:.0f}ms`")
            embed.add_field(name="サーバー名",value=f'`{ctx.guild.name}`')
            embed.add_field(name="現オーナー名",value=f'`{ctx.guild.owner}`')
            guild = ctx.guild
            member_count = sum(1 for member in guild.members if not member.bot) 
            bot_count = sum(1 for member in guild.members if member.bot) 
            all_count = (member_count) + (bot_count)
            embed.add_field(name="総人数",value=f'`{all_count}`',inline=False)
            embed.add_field(name="ユーザ数",value=f'`{member_count}`',inline=False)
            embed.add_field(name="BOT数",value=f'`{bot_count}`',inline=False)
            embed.add_field(name="テキストチャンネル数",value=f'`{len(ctx.guild.text_channels)}`',inline=False)
            embed.add_field(name="ボイスチャンネル数",value=f'`{len(ctx.guild.voice_channels)}`',inline=False)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)
            return
        server = self.bot.get_guild(server_id)
        embed = discord.Embed(title="鯖ステータス",description=f"Ping:`{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="サーバー名",value=f'`{server.name}`')
        embed.add_field(name="現オーナー名",value=f'`{server.owner}`')
        guild = server
        member_count = sum(1 for member in guild.members if not member.bot) 
        bot_count = sum(1 for member in guild.members if member.bot) 
        all_count = (member_count) + (bot_count)
        embed.add_field(name="総人数",value=f'`{all_count}`',inline=False)
        embed.add_field(name="ユーザ数",value=f'`{member_count}`',inline=False)
        embed.add_field(name="BOT数",value=f'`{bot_count}`',inline=False)
        embed.add_field(name="テキストチャンネル数",value=f'`{len(server.text_channels)}`',inline=False)
        embed.add_field(name="ボイスチャンネル数",value=f'`{len(server.voice_channels)}`',inline=False)
        embed.set_thumbnail(url=server.icon_url)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['b'])
    async def bot(self, ctx):
        embed = discord.Embed(title=f"{self.bot.user}", description="このBotの情報です")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="SERVERの数", value=f'`{len(self.bot.guilds)}`',inline=False)
        embed.add_field(name="USERの数", value=f'`{len(set(self.bot.get_all_members()))}`',inline=False)
        embed.add_field(name="言語", value='`discord.py`\n`discord.js`',inline=False)
        embed.add_field(name="Ping値", value=f'`{self.bot.ws.latency * 1000:.0f}ms`',inline=False)
        embed.add_field(name="各種リンク", value="[このBOTの公式開発鯖](<https://discord.gg/ENxnsJM>)", inline=False)
        await ctx.channel.send(embed=embed)
            
    #gbans a user with a reason
    @commands.command()
    async def gban(self, ctx, user_id: int=None, reason =None):
        if ctx.author.id != great_owner_id:
            return
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
    async def gunban(self, ctx, user_id: int=None, reason =None):
        if ctx.author.id != great_owner_id:
            return
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
    async def ban(self, ctx, user_id: int=None, reason =None):
        if user_id == None:
            await ctx.channel.send("BAN対象が正しくありません")
            return
        else:
            member = self.bot.get_user(user_id)
            print(member)
        banlog = self.bot.get_channel(694044656501129317)
        if member == ctx.message.author:
            await ctx.channel.send("BAN対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        await ctx.guild.ban(discord.Object(user_id), reason=reason)
        await ctx.channel.send(f"<@{user_id}> をBANしました。")
        await banlog.send(f"BAN通知 \n 鯖名：{ctx.guild.name} \n user id：{user_id} \n 理由：{reason}")
        print(member)

    #unbans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def unban(self, ctx, user_id: int=None, reason =None):
        if user_id == None:
            await ctx.channel.send("UNBAN対象が正しくありません")
            return
        else:
            member = self.bot.get_user(user_id)
            print(member)
        banlog = self.bot.get_channel(694044656501129317)
        if member == ctx.message.author:
            await ctx.channel.send("UNBAN対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        await ctx.guild.unban(discord.Object(user_id), reason=reason)
        await ctx.channel.send(f"<@{user_id}> をUNBANしました。")
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
        if message.content == '再起動して':
            await self.bot.logout()

    @commands.command(aliases=['sl'])
    async def slot(self, ctx, what: int=None):
        if what == None:
             what = 1
        coin_true = 0
        coin_none = 0
        coin_fals = 0
        slots = 1
        whats = what 
        what += 1
        while slots < what:
            if stopcodes == 1:
                await ctx.channel.send('停止します')
                slots = what
                stopcodes = 0
            suroto=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            suroto1=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            suroto2=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            await asyncio.sleep(0.1)
            my_message = await ctx.channel.send('？|？|？')
            await asyncio.sleep(0.5)
            await my_message.edit(content=suroto + '|？|？')
            await asyncio.sleep(0.5)
            await my_message.edit(content=suroto + '|' + suroto1 + '|？')
            await asyncio.sleep(0.5)
            await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2)
            if suroto == suroto1 == suroto2:
                await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：当たり！！')
                coin_true += 1
            elif suroto == suroto1 or suroto == suroto2 or suroto1 == suroto2:
                await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：リーチ！')
                coin_none += 1
            else:
                await my_message.edit(content=suroto + '|' + suroto1 + '|' + suroto2 + '\n 結果：ハズレ')
                coin_fals += 1
            slots += 1
        embed = discord.Embed(title="スロット結果",description=f"`Ping値:{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="試行回数",value=f'`{whats}`')
        embed.add_field(name="当たり回数", value=f'`{coin_true}`',inline=False)
        embed.add_field(name="リーチ回数", value=f'`{coin_none}`',inline=False)
        embed.add_field(name="ハズレ回数", value=f'`{coin_fals}`',inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['sl2'])
    async def slot2(self, ctx, what: int=None):
        if what == None:
             what = 1
        coin_true = 0
        coin_none = 0
        coin_fals = 0
        slot_count = await ctx.channel.send(f'0/{what} 完了')
        slots = 1
        whats = what 
        what += 1
        while slots < what:
            if stopcode == 1:
                await ctx.channel.send('停止します')
                slots = what
                stopcodes = 0
            suroto=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            suroto1=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            suroto2=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            await asyncio.sleep(0.1)
            if suroto == suroto1 == suroto2:
                coin_true += 1
            elif suroto == suroto1 or suroto == suroto2 or suroto1 == suroto2:
                coin_none += 1
            else:
                coin_fals += 1
            await asyncio.sleep(0.1)
            await slot_count.edit(content=f'{slots}/{whats} 完了')
            await asyncio.sleep(0.1)
            slots += 1
        embed = discord.Embed(title="スロット結果",description=f"`Ping値:{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="試行回数",value=f'`{whats}`')
        embed.add_field(name="当たり回数", value=f'`{coin_true}`',inline=False)
        embed.add_field(name="リーチ回数", value=f'`{coin_none}`',inline=False)
        embed.add_field(name="ハズレ回数", value=f'`{coin_fals}`',inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['sl3'])
    async def slot3(self, ctx, what: int=None):
        if what == None:
             what = 1
        coin_true = 0
        coin_none = 0
        coin_fals = 0
        slot_count = await ctx.channel.send(f'0/{what} 完了 \n`Ping値:{self.bot.ws.latency * 1000:.0f}ms`')
        slots = 1
        whats = what 
        what += 1
        while slots < what:
            if stopcode == 1:
                await ctx.channel.send('停止します')
                slots = what
                stopcodes = 0
            suroto=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            suroto1=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            suroto2=random.choice(('０', '１', '２', '３', '４', '５', '６', '７', '８', '９'))
            await asyncio.sleep(0.1)
            if suroto == suroto1 == suroto2:
                coin_true += 1
            elif suroto == suroto1 or suroto == suroto2 or suroto1 == suroto2:
                coin_none += 1
            else:
                coin_fals += 1
            await asyncio.sleep(0.1)
            await slot_count.edit(content=f'{slots}/{whats} 完了 \n`Ping値:{self.bot.ws.latency * 1000:.0f}ms`')
            await asyncio.sleep(0.1)
            slots += 1
        embed = discord.Embed(title="スロット結果",description=f"`Ping値:{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="試行回数",value=f'`{whats}`')
        embed.add_field(name="当たり回数", value=f'`{coin_true}`',inline=False)
        embed.add_field(name="リーチ回数", value=f'`{coin_none}`',inline=False)
        embed.add_field(name="ハズレ回数", value=f'`{coin_fals}`',inline=False)
        await ctx.channel.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
