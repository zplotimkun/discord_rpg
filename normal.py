import random

import discord
from dotenv import load_dotenv

load_dotenv()

def call_channl_user(client, GUILD, message):
    brooklyn_003_quotes = [
        ' 耖你媽你過來一下',
        ' 過來一下，給我過來一下',
        '嬰兒～～～～～～～',
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        '瑞斯一打三',
        '這什麼到底什麼閃現',
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

