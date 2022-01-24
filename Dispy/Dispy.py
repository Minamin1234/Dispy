from typing import NoReturn as void
from typing import List
from discord.channel import TextChannel
from discord.client import Client
from Compy import MCommand
from Compy import MModule
from Compy import MData
import discord
import json

#CompySubData class
class CData(MData):
    msg:discord.Message = None
    client:discord.Client = None
    disdev = None
    def __init__(self,newmsg:discord.Message=None,newclient:discord.Client=None,newdisdev=None):
        self.msg = newmsg
        self.client = newclient
        self.disdev = newdisdev
        return

#DispyModule class
class DModule(MModule):
    Disbot:discord.Client = None
    msg:discord.Message = None

    def __init__(self) -> void:
        self.ModuleName = "dmodule"
        return

#DispyDeveloper module
class DDev(DModule):
    def __init__(self,disbot:discord.Client) -> void:
        super().__init__()
        self.Disbot = disbot
        self.ModuleName = "dev"
        self.Commands = [
            "send",
            "sendall",
            "sendto",
            "stop",
            "setoutput",
            "help"
            ]
        return

    def ExecuteCommand(self,args:List[str],data:MData) -> str:
        result:str = ""
        if args[1] == self.Commands[0]:
            #dev.send([text])
            result = str(args[2])
        elif args[1] == self.Commands[1]:
            #dev.sendall([text])
            result = str(args[2])
        elif args[1] == self.Commands[2]:
            #dev.sendto([text],[channel_Id])
            result = str(args[2])
        elif args[1] == self.Commands[3]:
            #dev.stop()
            result = "stop..."
        elif args[1] == self.Commands[4]:
            #dev.setoutput()
            data.disdev.SetNewData(data.msg.guild.id,
                            data.msg.channel.id)
            result = "Set Output Channel: " + str(data.msg.guild) + " - " + str(data.msg.channel)
        elif args[1] == self.Commands[5]:
            #dev.help()
            result = self.ShowHelp()
        return result

#DispyData class
class DData(object):
    Server_Name:str = "server"
    Server_Id:int = 0
    Server_DefaultChannel_Id:int = 0

    def __init__(self,SName:str,SId:int,SChannelId:int) -> void:
        self.Server_Name = SName
        self.Server_Id = SId
        self.Server_DefaultChannel_Id = SChannelId
        return

    def ToDict(self) -> dict:
        dc:dict = {"Server_Name":self.Server_Name,
              "Server_Id":self.Server_Id,
              "Server_DefaultChannel_Id":self.Server_DefaultChannel_Id
              }
        return dc

    def ToJSON(self) -> bool:
        return True

#'M'inamin's'Dis'cordbotOn'Py'thon class
class MDispy(MCommand):
    msg:discord.Message = None
    Datas:List[DData] = []
    def __init__(self) -> void:
        super().__init__()
        client = discord.Client()
        return

    def SetMsg(self,newmsg:discord.Message):
        self.msg = newmsg
        for module in self.Modules:
            if isinstance(module,DModule):
                module.msg = newmsg
        return

#DataControl
    def Search(self,SId:int) -> DData:
        for data in self.Datas:
            if data.Server_Id == Sid:
                return data
        return None

    def AddNewData(self,newSName:str,newSId:int,newSChannelId:int) -> bool:
        for data in self.Datas:
            if data.Server_Id == data:
                return False
        newdata = DData(newSName,newSId,newSChannelId)
        self.Datas.append(newdata)
        return True

    def SetNewData(self,TargetSId:int,newSChId:int) -> bool:
        for data in self.Datas:
            if data.Server_Id == TargetSId:
                data.Server_DefaultChannel_Id = newSChId
                return True
        return False

    def LoadDataListFromJSON(self,path:str) -> bool:
        datas:dict = {}
        self.Datas = []
        try:
            with open(path,"r") as f:
                datas = json.load(f)
        except FileNotFoundError:
            return False
        for data in datas.values():
            newdata:DData = DData(str(data["Server_Name"]),
                                  int(data["Server_Id"]),
                                  int(data["Server_DefaultChannel_Id"]))
            self.Datas.append(newdata)
        return True

    def Save(self,path:str) -> bool:
        datas:dict = {}
        idx:int = 0
        for data in self.Datas:
            datas[str(idx)] = data.ToDict()
            idx += 1
        with open(path,"w") as f:
            json.dump(datas,f,ensure_ascii=False)
        return True

    def InitializeCollect(self,client:discord.Client) -> bool:
        firstch:discord.TextChannel = None
        #print(self.Datas)
        for server in client.guilds:
            for ch in server.channels:
                if type(ch) is discord.TextChannel:
                    firstch = ch
                    break
            newdata = DData(server.name,server.id,firstch.id)
            self.Datas.append(newdata)