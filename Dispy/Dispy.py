from typing import NoReturn as void
from typing import List

from discord.client import Client
from Compy import MCommand
from Compy import MModule
import discord

class DModule(MModule):
    Disbot:discord.Client = None
    msg:discord.Message = None

    def __init__(self) -> void:
        self.ModuleName = "dmodule"
        return

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
            "help"
            ]
        return

    def ExecuteCommand(self,args:List[str]) -> str:
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
            self.Disbot.loop.stop()
        elif args[1] == self.Commands[4]:
            #dev.help()
            result = self.ShowHelp()
        return result

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