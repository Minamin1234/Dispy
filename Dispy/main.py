import discord
from Dispy import Dispy

client = discord.Client();
Token = 'ODgzMzc4MTAzNjM4OTYyMjU2.YTJD-A.6lmBAZzWQ98o6Ve9cXWkEEuxp6g'
CommandWord:str = "!c "
CommandDevice:Dispy = Dispy()

@client.event
async def on_ready():
    print("Active.")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(CommandWord):
        CommandDevice.SetMsg(message)
        word:str = message.content.rstrip("!c ")
        CommandDevice.Execute(word)

client.run(Token)