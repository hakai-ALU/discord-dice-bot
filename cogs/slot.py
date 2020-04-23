from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class slot(commands.Cog):
    # slotクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
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
        hundreds = 100
        coin_true_co = coin_true * hundreds // whats
        coin_none_co = coin_none * hundreds // whats
        coin_fals_co = coin_fals * hundreds // whats
        embed = discord.Embed(title="スロット結果",description=f"`Ping値:{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="試行回数",value=f'`{whats}`')
        embed.add_field(name="当たり回数", value=f'`{coin_true}({coin_true_co}%)`',inline=False)
        embed.add_field(name="リーチ回数", value=f'`{coin_none}({coin_none_co}%)`',inline=False)
        embed.add_field(name="ハズレ回数", value=f'`{coin_fals}({coin_fals_co}%)`',inline=False)
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
        hundreds = 100
        coin_true_co = coin_true * hundreds // whats
        coin_none_co = coin_none * hundreds // whats
        coin_fals_co = coin_fals * hundreds // whats
        embed = discord.Embed(title="スロット結果",description=f"`Ping値:{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="試行回数",value=f'`{whats}`')
        embed.add_field(name="当たり回数", value=f'`{coin_true}({coin_true_co}%)`',inline=False)
        embed.add_field(name="リーチ回数", value=f'`{coin_none}({coin_none_co}%)`',inline=False)
        embed.add_field(name="ハズレ回数", value=f'`{coin_fals}({coin_fals_co}%)`',inline=False)
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
        hundreds = 100
        coin_true_co = coin_true * hundreds // whats
        coin_none_co = coin_none * hundreds // whats
        coin_fals_co = coin_fals * hundreds // whats
        embed = discord.Embed(title="スロット結果",description=f"`Ping値:{self.bot.ws.latency * 1000:.0f}ms`")
        embed.add_field(name="試行回数",value=f'`{whats}`')
        embed.add_field(name="当たり回数", value=f'`{coin_true}({coin_true_co}%)`',inline=False)
        embed.add_field(name="リーチ回数", value=f'`{coin_none}({coin_none_co}%)`',inline=False)
        embed.add_field(name="ハズレ回数", value=f'`{coin_fals}({coin_fals_co}%)`',inline=False)
        await ctx.channel.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(slot(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
