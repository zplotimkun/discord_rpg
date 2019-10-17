import os
import random

from story import  main_story
from normal import call_channl_user

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

##當機器人啟動 會print出機器人加入discord
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

## 當有用戶加入頻道 會私訊用戶
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

## 機器人回話
@client.event
async def on_message(message):
    if message.author == client.user and message.content.startswith('!'):
        return

    if '!呼叫:' in message.content.lower():
        await message.channel.send(call_channl_user(client, GUILD, message))

    if '!故事前述' == message.content.lower():
        before_story = main_story()
        await message.channel.send(before_story)

    if '!help' == message.content.lower():
        pass



    ## 範例：當有會員說出生日快樂 機器人會說生日快樂
    if 'happy birthday' in message.content.lower():
        if message.author == client.user:
            return
        await message.channel.send('Happy Birthday! 🎈🎉')



client.run(token)