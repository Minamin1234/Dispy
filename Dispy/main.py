import discord
from Dispy import MDispy
from Dispy import DDev

Developer_Id:int = 834758459349925939

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
        if args[0] == "dev":
            if message.author.id != Developer_Id:
                await message.channel.send("Can't execute command: Developer Only")
                return
            if args[1] == "send":
                await message.channel.send(str(args[2]))
                return
            elif args[1] == "sendall":
                return
            elif args[1] == "sendto":
                return
            elif args[1] == "help":
                result = CommandDevice.Execute(word)
        await message.channel.send(">>" + str(result))

client.run(Token)
