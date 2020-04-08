from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):
    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        self.stopcodes = 0

    @commands.command(aliases=['sc'])
    async def stopcode(self, ctx, stop_code: int=None):
        if ctx.author.id != great_owner_id:
            return
        if stop_code == None:
            SCP = self.stopcodes
            await ctx.send(f'Stop Codeが指定されていません。\n`Stop Code={SCP}`')
            return
        self.stopcodes = stop_code
        await ctx.send(f'Stop Codeを設定しました。\n`Stop Code={self.stopcodes}`')

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

    @commands.Cog.listener()
    @commands.has_permissions(manage_guild=True)
    async def on_message(self, message):
        if message.author.id == 159985870458322944: # MEE6からのメッセージかどうかを判別
            if message.content.startswith("!levelup"):
                level = int(message.content.split()[-2]) # メッセージを分解
                t_name = message.content.split()[-1] # メッセージを分解
                target = discord.utils.get(message.server.members, mention=t_name) # レベルアップしたユーザーのIDを取得
                levels = 10 - str(level)
                replys = f"{t_name}さん、が{str(level)}レベルになりました。\nあと{levels}で上級市民になります。" # レベルアップメッセージ
                await self.bot.get_channel(695795193244286997).send(replys)

                if level == 10: # レベル1になった時の処理
                    levelrole1 = discord.utils.get(message.server.roles, name="上級市民")
                    await target.add_roles(levelrole1)
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
        if self.stopcodes != 0:
            await ctx.channel.send('⚠️現在使用できません⚠️')
            return
        if what == None:
            what = 1
        coin_true = 0
        coin_none = 0
        coin_fals = 0
        slots = 1
        whats = what 
        what += 1
        while slots < what:
            if self.stopcodes != 0:
                stp = await ctx.channel.send('停止します')
                slots = what
                if self.stopcodes == 9:
                    await stp.edit(content='⚠️現在使用できません⚠️')
                    return
                self.stopcodes = 0
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
        if self.stopcodes != 0:
            await ctx.channel.send('⚠️現在使用できません⚠️')
            return
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
            if self.stopcodes != 0:
                stp = await ctx.channel.send('停止します')
                slots = what
                if self.stopcodes == 9:
                    await stp.edit(content='⚠️現在使用できません⚠️')
                    return
                self.stopcodes = 0
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
        if self.stopcodes != 0:
            await ctx.channel.send('⚠️現在使用できません⚠️')
            return
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
            if self.stopcodes != 0:
                stp = await ctx.channel.send('停止します')
                slots = what
                if self.stopcodes == 9:
                    await stp.edit(content='⚠️現在使用できません⚠️')
                    return
                self.stopcodes = 0
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

    # メインとなるroleコマンド
    @commands.group(aliases=['rl'])
    @commands.has_permissions(manage_guild=True)
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
    async def create(self, ctx, what= None):
        if what == None:
            await ctx.send('Error:type name=None')
            return
        rote = 0
        hoist = False
        mentionable = False
        administrator = False
        view_audit_log = False
        manage_guild = False
        manage_roles = False
        manage_channels = False
        kick_members = False
        ban_members = False
        create_instant_invite = False
        change_nicknames = False
        manage_nicknames = False
        manage_emojis = False
        manage_webhooks = False
        use_voice_activation = False
        read_messages = False
        while rote < 2:
            roleedit = discord.Embed(title="権限設定",description=f"番号を入力して下さい。")
            roleedit.add_field(name=f"**オンラインメンバーとは別にロールメンバーを表示する({hoist})**",value='`a`')
            roleedit.add_field(name=f"**このロールに対して@mentionを許可する({mentionable})**",value='`b`')
            roleedit.add_field(name=f"**管理者({administrator})**",value='`1`')
            roleedit.add_field(name=f"**監査ログを表示({view_audit_log})**",value='`2`')
            roleedit.add_field(name=f"**サーバーの管理({manage_guild})**",value='`3`')
            roleedit.add_field(name=f"**ロールの管理({manage_roles})**",value='`4`')
            roleedit.add_field(name=f"**チャンネルの管理({manage_channels})**",value='`5`')
            roleedit.add_field(name=f"**メンバーをKICK({kick_members})**",value='`6`')
            roleedit.add_field(name=f"**メンバーをBAN({ban_members})**",value='`7`')
            roleedit.add_field(name=f"**招待を作成({create_instant_invite})**",value='`8`')
            roleedit.add_field(name=f"**ニックネームの変更({change_nicknames})**",value='`9`')
            roleedit.add_field(name=f"**ニックネームの管理({manage_nicknames})**",value='`10`')
            roleedit.add_field(name=f"**絵文字の管理({manage_emojis})**",value='`11`')
            roleedit.add_field(name=f"**ウェブフックの管理({manage_webhooks})**",value='`12`')
            roleedit.add_field(name=f"**テキストチャンネルの閲覧&ボイスチャンネルの表示({read_messages})**",value='`13`')
            roleedit.add_field(name="－－－－－－－－－－",value='－－－－－－－－－－')
            roleedit.add_field(name="**無付与・設定完了**",value='`0`')
            await ctx.channel.send(embed=roleedit) 
            def  rotetime(m):
                return m.content == "a" or "b" or "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" and m.author == ctx.author
            try:
                reply = await self.bot.wait_for( "message" , check = rotetime , timeout = 300.0 )
            except asyncio.TimeoutError:
                await ctx.channel.send( "設定を中止します。(type:time over)" )
                return
            else:
                if reply.content == "0":
                    rote = 2
                elif reply.content == "a":
                    hoist = True
                    rote = 0
                elif reply.content == "b":
                    mentionable = True
                    rote = 0
                elif reply.content == "1":
                    administrator = True
                    rote = 0
                elif reply.content == "2":
                    view_audit_log = True
                    rote = 0
                elif reply.content == "3":
                    manage_guild = True
                    rote = 0
                elif reply.content == "4":
                    manage_roles = True
                    rote = 0
                elif reply.content == "5":
                    manage_channels = True
                    rote = 0
                elif reply.content == "6":
                    kick_members = True
                    rote = 0
                elif reply.content == "7":
                    ban_members = True
                    rote = 0
                elif reply.content == "8":
                    create_instant_invite = True
                    rote = 0
                elif reply.content == "9":
                    change_nicknames = True
                    rote = 0
                elif reply.content == "10":
                    manage_nicknames = True
                    rote = 0
                elif reply.content == "11":
                    manage_emojis = True
                    rote = 0
                elif reply.content == "12":
                    manage_webhooks = True
                    rote = 0
                elif reply.content == "13":
                    read_messages = True
                    use_voice_activation = True
                    rote = 0
                
        pre = discord.Permissions(administrator=administrator,view_audit_log=view_audit_log,manage_guild=manage_guild,manage_roles=manage_roles,manage_channels=manage_channels,kick_members=kick_members,ban_members=ban_members,create_instant_invite=create_instant_invite,change_nickname=change_nicknames,manage_nicknames=manage_nicknames,manage_emojis=manage_emojis,manage_webhooks=manage_webhooks,read_messages=read_messages,use_voice_activation=use_voice_activation)       
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2,hoist=hoist,mentionable=mentionable,permissions=pre)
        await ctx.send(f'作成しました。@' + set_name2)
        
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
