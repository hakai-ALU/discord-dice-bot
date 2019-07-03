import discord 
import os
import asyncio
from datetime import datetime

class ScheduleTime:
  def __init__(self, weekday, hourTime, minutesTime):
    self.Weekday = weekday
    self.HourTime = hourTime
    self.MinutesTime = minutesTime

  def edit_Weekday(self, weekday):
    self.Weekday = weekday
    pass

  def edit_HourTime(self, hourTime):
    self.HourTime = hourTime
    pass

  def edit_MinutesTime(self, minutesTime):
    self.MinutesTime = minutesTime
    pass

  def edit_AllValue(self, weekday, hourTime, minutesTime):
    self.edit_Weekday(int(weekday))
    self.edit_HourTime(int(hourTime))
    self.edit_MinutesTime(int(minutesTime))
    pass

  def is_match(firstValue, secondValue):
    if firstValue.Weekday != secondValue.Weekday :
      return False
    if firstValue.HourTime != secondValue.HourTime :
      return False
    if firstValue.MinutesTime != secondValue.MinutesTime :
      return False
    return True

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
StartTime = ScheduleTime(0,10,0)  # 集計開始
EndTime = ScheduleTime(2,23,59)   # 集計おわり
week = ['月','火','水','木','金','土','日']
commandList = {
  '/help':0,
  '/start':3,
  '/end':3,
  '/check':1
}
part = 0
isStartSended = False
isEndSended = False

@asyncio.coroutine
def SendMsg(Channel, msg):
  print('reply = '+ msg)
  if msg != '':
    yield from client.send_message(Channel, msg)
  pass

@asyncio.coroutine
async def check_for_reminder():
  while  True:
    await asyncio.sleep(3)
    now = datetime.now()
    currentTime = ScheduleTime(now.weekday(), now.hour, now.minute)

    if ScheduleTime.is_match(StartTime, currentTime):
      global isStartSended
      global part
      if not isStartSended:
        part = 0
        StartText = '今週の活動は、{}月{}日です。\n参加する方は、リアクションをお願いします。\n投票は{}曜日に無慈悲に締め切ります。'.format(datetime.now().month, datetime.now().day + 4, week[int(EndTime.Weekday)])
        await SendMsg(DefaultChannel, StartText)
        isStartSended = True
    else:
      isStartSended = False

    if ScheduleTime.is_match(EndTime, currentTime):
      global isEndSended
      if not isEndSended:
        global part
        EndText = '今週の参加登録を締め切りました。参加人数は{}人です！！'.format(part)
        await SendMsg(DefaultChannel, EndText)
        isEndSended = True
    else:
      isEndSended = False

@asyncio.coroutine
def main_task():
  print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
  yield from client.start(token)
  pass


def botCommand(command, contents):
  SendMsg =''
  if  command not in commandList:
    return 'そんなコマンドはないよ？ /help で確認してね'
  if len(contents) != commandList[command]:
    return '要素の数がおかしいよ？もう一度確認してね！'
  if command == '/start':
    StartTime.edit_AllValue(contents[0],contents[1],contents[2])
    SendMsg = '投票開始の時間を{}曜日の{}時{}分にセットしました。'.format(week[int(contents[0])],contents[1],contents[2])
  elif command == '/end':
    EndTime.edit_AllValue(contents[0],contents[1],contents[2])
    SendMsg = '投票終わりの時間を{}曜日の{}時{}分にセットしました。'.format(week[int(contents[0])],contents[1],contents[2])
  elif command == '/check':
    if contents[0] == 'start':
      SendMsg = '投票開始時間は、{}曜日{}時{}分に設定されています。'.format(week[int(StartTime.Weekday)],StartTime.HourTime,StartTime.MinutesTime)
    elif contents[0] == 'end':
      SendMsg = '投票終了時間は、{}曜日{}時{}分に設定されています。'.format(week[int(EndTime.Weekday)],EndTime.HourTime,EndTime.MinutesTime)
    elif contents[0] == 'people':
      global part
      SendMsg = '現在の参加人数は、{}人です。'.format(part)
    else:
      SendMsg = 'コマンドを確認してね！'
    pass
  else :
    SendMsg = 'コマンドを確認してね！'
  return SendMsg

# Discord Event
@client.event
async def on_ready():
  global DebugChannel
  global DefaultChannel
  DebugChannel = client.get_channel(DebugId)
  DefaultChannel = client.get_channel(DefaultId)
  await SendMsg(DebugChannel, 'ログインしました')
  pass

@client.event
async def on_message(message):
  # メッセージの送り主がBotならなにもしない
  if client.user == message.author:
    return
  contents = message.content.split(' ')
  bot_command = str(contents[0]).lower()
  contents = contents[1:]
  contents = [str(content) for content in contents]
  reply = botCommand(bot_command, contents)
  if message.channel.name == "bot":
    await SendMsg(message.channel, reply)
  pass

@client.event
async def on_reaction_add(reaction, user):
    global part
    if reaction.message.author == client.user:
        part += 1
        print('part = '+ str(part))
        await SendMsg(DefaultChannel, f'{user.mention} 参加登録しました。')


@client.event
async def on_reaction_remove(reaction, user):
    global part
    if reaction.message.author == client.user:
        part -= 1
        await SendMsg(DefaultChannel, f'{user.mention} 参加をキャンセルしました。')
    pass

client.run(TOKEN)
