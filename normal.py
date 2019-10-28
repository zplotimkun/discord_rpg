import random

import discord
from dotenv import load_dotenv

load_dotenv()

def call_channl_user(client, GUILD, message):
    brooklyn_003_quotes = [
        ' 耖你媽你過來一下',
        ' 過來一下，給我過來一下',
        ' 嬰兒～～～～～～～',
        ' AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        ' 瑞斯一打三',
        ' 這什麼到底什麼閃現',
    ]

    if '!呼叫:' in message.content.lower():
        call_user = message.content[4:]
        for guild in client.guilds:
            if guild.name == GUILD:
                break
        for m in message.guild.members:
            if call_user == str(m).split('#')[0]:
                
                response = '{} {}'.format(m.mention, random.choice(brooklyn_003_quotes))
        
        return(response)

def instruction_help():
    help_detail = []

    help_detail.append('1. {!呼叫:} 使用方式為後面加名稱 ex: !呼叫:勇士搖搖樂')
    help_detail.append('2. {!故事前述} 為遊戲前述')
    help_detail.append('3. {!happy birthday} 只要有就會回話')


    return(help_detail)
