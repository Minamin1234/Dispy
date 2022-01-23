import discord
from Dispy import MDispy

client = discord.Client();
Token = 'ODgzMzc4MTAzNjM4OTYyMjU2.YTJD-A.6lmBAZzWQ98o6Ve9cXWkEEuxp6g'
CommandWord:str = "!c "
CommandDevice:MDispy = MDispy()

@client.event
async def on_ready():
    print("Active.")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(CommandWord):
        word:str = message.content.lstrip("!c ")
        result:str = CommandDevice.Execute(word)
        await message.channel.send(result)

client.run(Token)