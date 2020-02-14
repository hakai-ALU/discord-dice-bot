from discord.ext import commands # Bot Commands Frameworkをインポート
import traceback # エラー表示のためにインポート
import os
import discord

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 665579602504318978

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.testcog'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class MyBot(commands.Bot):

    # MyBotのコンストラクタ。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print(self.user.name)  # ボットの名前
        print(self.user.id)  # ボットのID
        print(discord.__version__)  # discord.pyのバージョン
        print('----------------')
        print('Hello World,リマインドbotプログラム「project-RRN」、起動しました')
        channel = self.get_channel(CHANNEL_ID)
        await channel.purge()
        await channel.send(f'名前:{self.user.name}')  # ボットの名前
        await channel.send(f'ID:{self.user.id}')  # ボットのID
        await channel.send(f'Discord ver:{discord.__version__}')  # discord.pyのバージョン
        await channel.send('----------------')
        await channel.send('状態：BOT再起動しました。')   
        await self.change_presence(status=discord.Status.idle,activity=discord.Game(name='Discord Test Program'))
        bot.load_extension("cogs.dtp")

# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    bot = MyBot(command_prefix='rn!') # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(TOKEN) # Botのトークン
