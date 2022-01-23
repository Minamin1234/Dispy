import discord
from Dispy import MDispy
from Dispy import DDev


client = discord.Client();
Token = 'ODgzMzc4MTAzNjM4OTYyMjU2.YTJD-A.6lmBAZzWQ98o6Ve9cXWkEEuxp6g'
CommandWord:str = "!c "
CommandDevice:MDispy = MDispy()
ddev:DDev = DDev(client)
CommandDevice.IncludeNewModule(ddev)


@client.event
async def on_ready():
    print("Active.")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(CommandWord):
        word:str = message.content.lstrip(CommandWord)
        args:List[str] = CommandDevice.DecodeArgs(word)

        CommandDevice.SetMsg(message)
        result:str = CommandDevice.Execute(word)
        await message.channel.send(">>" + str(result))

client.run(Token)
