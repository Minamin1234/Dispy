import discord
from Compy import MResult
from Dispy import MDispy
from Dispy import DDev
from Dispy import CData
import json

PriPath:str = "Private.json"
PriData:dict = {}
with open(PriPath,"r") as f:
    PriData = json.load(f)

Developer_Id:int = int(PriData["Developer_Id"])
Token:str = str(PriData["Token"])
CommandWord:str = "!c "
Path:str = "Data.json"

client = discord.Client();
CommandDevice:MDispy = MDispy()
ddev:DDev = DDev(client)
CommandDevice.IncludeNewModule(ddev)



@client.event
async def on_ready():
    print("Active.")
    print(client.guilds)
    if CommandDevice.LoadDataListFromJSON(Path) == False:
        CommandDevice.InitializeCollect(client)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(CommandWord):
        data:CData = CData(message,client,CommandDevice)
        word:str = message.content.lstrip(CommandWord)
        args:List[str] = CommandDevice.DecodeArgs(word)
        CommandDevice.SetMsg(message)
        cresult:CResult = CommandDevice.Execute(word,data)
        dtxchId:int = CommandDevice.Search(message.guild.id).Server_DefaultChannel_Id
        cresult.TxtChannel = client.get_channel(dtxchId)
        result:str = cresult.Result
        print(type(cresult))
        if args[0] == "dev":
            if message.author.id != Developer_Id:
                text = "Can't execute command: Developer Only\n"
                text += "あなたは開発者権限がないため，このコマンドは実行できません．"
                await message.channel.send(text)
                return

            if args[1] == "send":
                await message.channel.send(str(args[2]))
                return
            elif args[1] == "sendall":
                for tch in cresult.TxtChannels:
                    await tch.send(str(args[2]))
                return
            elif args[1] == "sendto":
                pass
            elif args[1] == "stop":
                await message.channel.send(">>" + str(result))
                await client.close()
                return
            elif args[1] == "help":
                result = CommandDevice.Execute(word,data).Result

            await cresult.TxtChannel.send(result)
            return

        await cresult.TxtChannel.send(result)
        

client.run(Token)
CommandDevice.Save(Path)
