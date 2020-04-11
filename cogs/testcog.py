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
        """ストップコード(開発者用)"""
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
        """オウム返し"""
        await ctx.send(f'{what}')

    @commands.command(aliases=['t'])
    async def test(self, ctx, user_id: discord.Object):
        """オウム返し"""
        memberss = user_id #self.bot.get_user(user_id)
        await ctx.send(f'{memberss}')
        await ctx.send(f'{memberss.name}')
        await ctx.send(f'{memberss.id}')
        await ctx.send(f'{memberss.created_at}')
        
    @commands.command(aliases=['sinfo'])
    async def serverinfo(self, ctx, server_id: int=None):
        """鯖について"""
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
        """Botについて"""
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
        """グローバルBan(開発者用)"""
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
        """グローバルUnBan(開発者用)"""
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
        """Ban(管理者用)"""
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
        """UnBan(管理者用)"""
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
        """Kick(管理者用)"""
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
        """スロット"""
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
        """スロット(Not出力)"""
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
        """スロット(Not出力&毎Ping値)"""
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
        """役職関連(管理者用)"""
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['ad'])
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        """付与(管理者用)"""
        await member.add_roles(role)
        await ctx.send('付与しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command(aliases=['rm'])
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        """剥奪(管理者用)"""
        await member.remove_roles(role)
        await ctx.send('剥奪しました。')

    # roleコマンドのサブコマンド
    # 指定した役職を削除する。
    @role.command(aliases=['dl'])
    async def delete(self, ctx, role: discord.Role=None):
        """削除(管理者用)"""
        if role == None:
            await ctx.send('役職名を指定して下さい。')
            return
        #role = discord.utils.get(ctx.guild.roles, name=role_name)
        await role.delete()
        await ctx.send('削除しました。')

    # roleコマンドのサブコマンド
    # 役職を作成する。
    @role.command(aliases=['cr'])
    async def create(self, ctx, what= None):
        """作成(管理者用)"""
        if what == None:
            what = "new role"
        rote = 0
        #システム
        hoist = False
        mentionable = False
        #基本権限
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
        read_messages = False
        #テキスト権限
        send_messages = False
        send_tts_messages = False
        manage_messages = False
        embed_links = False
        attach_files = False
        read_message_history = False
        mention_everyone = False
        external_emojis = False
        add_reactions = False
        #ボイス権限
        connect = False
        speak = False
        mute_members = False
        deafen_members = False
        move_members = False
        use_voice_activation = False
        while rote < 2:
            roleedit = discord.Embed(title="権限設定",description=f"番号・記号を入力して下さい。")
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
            if read_messages == True:
                await asyncio.sleep(0.1)
                roletxt = discord.Embed(title="テキストの権限",description=f"番号を入力して下さい。")
                roletxt.add_field(name=f"**メッセージを送信({send_messages})**",value='`14`')
                roletxt.add_field(name=f"**TTSメッセージを送信({send_tts_messages})**",value='`15`')
                roletxt.add_field(name=f"**メッセージの管理({manage_messages})**",value='`16`')
                roletxt.add_field(name=f"**埋め込みリンク({embed_links})**",value='`17`')
                roletxt.add_field(name=f"**ファイルの添付({attach_files})**",value='`18`')
                roletxt.add_field(name=f"**メッセージ履歴を読む({read_message_history})**",value='`19`')
                roletxt.add_field(name=f"**@everyone,@here,すべてのロールにメンション({mention_everyone})**",value='`20`')
                roletxt.add_field(name=f"**外部の絵文字の使用({external_emojis})**",value='`21`')
                roletxt.add_field(name=f"**リアクションの追加({add_reactions})**",value='`22`')
                roletxt.add_field(name="－－－－－－－－－－",value='－－－－－－－－－－')
                roletxt.add_field(name="**無付与・設定完了**",value='`0`')
                await ctx.channel.send(embed=roletxt) 
                await asyncio.sleep(0.1)
                rolevoc = discord.Embed(title="音声の権限",description=f"番号を入力して下さい。")
                rolevoc.add_field(name=f"**接続({connect})**",value='`23`')
                rolevoc.add_field(name=f"**発言({speak})**",value='`24`')
                rolevoc.add_field(name=f"**メンバーをミュート({mute_members})**",value='`25`')
                rolevoc.add_field(name=f"**メンバーのスピーカーをミュート({deafen_members})**",value='`26`')
                rolevoc.add_field(name=f"**メンバーを移動({move_members})**",value='`27`')
                rolevoc.add_field(name=f"**音声検出を使用({use_voice_activation})**",value='`28`')
                rolevoc.add_field(name="－－－－－－－－－－",value='－－－－－－－－－－')
                rolevoc.add_field(name="**無付与・設定完了**",value='`0`')
                await ctx.channel.send(embed=rolevoc) 
            def  rotetime(m):
                return m.content == "a" or "b" or "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14" or "15" or "16" or "17" or "18" "19" or "20" or "21" or "22" or "23" or "24" or "25" or "26" or "27" or "28" and m.author == ctx.author
            try:
                reply = await self.bot.wait_for( "message" , check = rotetime , timeout = 300.0 )
            except asyncio.TimeoutError:
                await ctx.channel.send( "設定を中止します。(type:time over)" )
                return
            else:
                if reply.content == "0":
                    rote = 2
                elif reply.content == "a":
                    if hoist == False:
                        hoist = True
                    elif hoist == True:
                        hoist = False
                    rote = 0
                elif reply.content == "b":
                    if mentionable == False:
                        mentionable = True
                    elif mentionable == True:
                        mentionable = False
                    rote = 0
                elif reply.content == "1":
                    if administrator == False:
                        administrator = True
                    elif administrator == True:
                        administrator = False
                    rote = 0
                elif reply.content == "2":
                    if view_audit_log == False:
                        view_audit_log = True
                    elif view_audit_log == True:
                        view_audit_log = False
                    rote = 0
                elif reply.content == "3":
                    if manage_guild == False:
                        manage_guild = True
                    elif manage_guild == True:
                        manage_guild = False
                    rote = 0
                elif reply.content == "4":
                    if manage_roles == False:
                        manage_roles = True
                    elif manage_roles == True:
                        manage_roles = False
                    rote = 0
                elif reply.content == "5":
                    if manage_channels == False:
                        manage_channels = True
                    elif manage_channels == True:
                        manage_channels = False
                    rote = 0
                elif reply.content == "6":
                    if kick_members == False:
                        kick_members = True
                    elif kick_members == True:
                        kick_members = False
                    rote = 0
                elif reply.content == "7":
                    if ban_members == False:
                        ban_members = True
                    elif ban_members == True:
                        ban_members = False
                    rote = 0
                elif reply.content == "8":
                    if create_instant_invite == False:
                        create_instant_invite = True
                    elif create_instant_invite == True:
                        create_instant_invite = False
                    rote = 0
                elif reply.content == "9":
                    if change_nicknames == False:
                        change_nicknames = True
                    elif change_nicknames == True:
                        change_nicknames = False
                    rote = 0
                elif reply.content == "10":
                    if manage_nicknames == False:
                        manage_nicknames = True
                    elif manage_nicknames == True:
                        manage_nicknames = False
                    rote = 0
                elif reply.content == "11":
                    if manage_emojis == False:
                        manage_emojis = True
                    elif manage_emojis == True:
                        manage_emojis = False
                    rote = 0
                elif reply.content == "12":
                    if manage_webhooks == False:
                        manage_webhooks = True
                    elif manage_webhooks == True:
                        manage_webhooks = False
                    rote = 0
                elif reply.content == "13":
                    if read_messages == False:
                        read_messages = True
                    elif read_messages == True:
                        read_messages = False
                        send_messages = False
                        send_tts_messages = False
                        manage_messages = False
                        embed_links = False
                        attach_files = False
                        read_message_history = False
                        mention_everyone = False
                        external_emojis = False
                        add_reactions = False
                        connect = False
                        speak = False
                        mute_members = False
                        deafen_members = False
                        move_members = False
                        use_voice_activation = False
                    rote = 0
                elif reply.content == "14":
                    if send_messages == False:
                        send_messages = True
                    elif send_messages == True:
                        send_messages = False
                    rote = 0
                elif reply.content == "15":
                    if send_tts_messages == False:
                        send_tts_messages = True
                    elif send_tts_messages == True:
                        send_tts_messages = False
                    rote = 0
                elif reply.content == "16":
                    if manage_messages == False:
                        manage_messages = True
                    elif manage_messages == True:
                        manage_messages = False
                    rote = 0
                elif reply.content == "17":
                    if embed_links == False:
                        embed_links = True
                    elif embed_links == True:
                        embed_links = False
                    rote = 0
                elif reply.content == "18":
                    if attach_files == False:
                        attach_files = True
                    elif attach_files == True:
                        attach_files = False
                    rote = 0
                elif reply.content == "19":
                    if read_message_history == False:
                        read_message_history = True
                    elif read_message_history == True:
                        read_message_history = False
                    rote = 0
                elif reply.content == "20":
                    if mention_everyone == False:
                        mention_everyone = True
                    elif mention_everyone == True:
                        mention_everyone = False
                    rote = 0
                elif reply.content == "21":
                    if external_emojis == False:
                        external_emojis = True
                    elif external_emojis == True:
                        external_emojis = False
                    rote = 0
                elif reply.content == "22":
                    if add_reactions == False:
                        add_reactions = True
                    elif add_reactions == True:
                        add_reactions = False
                    rote = 0
                elif reply.content == "23":
                    if connect == False:
                        connect = True
                    elif connect == True:
                        connect = False
                    rote = 0
                elif reply.content == "24":
                    if speak == False:
                        speak = True
                    elif speak == True:
                        speak = False
                    rote = 0
                elif reply.content == "25":
                    if mute_members == False:
                        mute_members = True
                    elif mute_members == True:
                        mute_members = False
                    rote = 0
                elif reply.content == "26":
                    if deafen_members == False:
                        deafen_members = True
                    elif deafen_members == True:
                        deafen_members = False
                    rote = 0
                elif reply.content == "27":
                    if move_members == False:
                        move_members = True
                    elif move_members == True:
                        move_members = False
                    rote = 0
                elif reply.content == "28":
                    if use_voice_activation == False:
                        use_voice_activation = True
                    elif use_voice_activation == True:
                        use_voice_activation = False
                    rote = 0
                
        pre = discord.Permissions(administrator=administrator,view_audit_log=view_audit_log,manage_guild=manage_guild,manage_roles=manage_roles,manage_channels=manage_channels,kick_members=kick_members,ban_members=ban_members,create_instant_invite=create_instant_invite,change_nickname=change_nicknames,manage_nicknames=manage_nicknames,manage_emojis=manage_emojis,manage_webhooks=manage_webhooks,read_messages=read_messages,send_messages=send_messages,
                                  send_tts_messages=send_tts_messages,manage_messages=manage_messages,embed_links=embed_links,attach_files=attach_files,read_message_history=read_message_history,mention_everyone=mention_everyone,external_emojis=external_emojis,add_reactions=add_reactions,
                                  connect=connect,speak=speak,mute_members=mute_members,deafen_members=deafen_members,move_members=move_members,use_voice_activation=use_voice_activation)       
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2,hoist=hoist,mentionable=mentionable,permissions=pre)
        await ctx.send(f'作成しました。@' + set_name2)
        
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
