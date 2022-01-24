from typing import NoReturn as void
from typing import List
from discord.channel import TextChannel
from discord.client import Client
from Compy import MCommand
from Compy import MModule
from Compy import MData
import discord
import json

Version:str = "v1.0beta"

#CompySubData class
#コマンドクラスDispy用のコマンド実行時に渡す補助データクラス．
#継承すれば，様々なデータを含めてコマンドモジュール側に渡す事が出来る．
class CData(MData):
    #ユーザから送信されたメッセージの情報．
    msg:discord.Message = None
    #ボットの情報
    client:discord.Client = None
    #このデータを所有するコマンドクラス（Dispy型）
    disdev = None
    def __init__(self,newmsg:discord.Message=None,newclient:discord.Client=None,newdisdev=None):
        self.msg = newmsg
        self.client = newclient
        self.disdev = newdisdev
        return

#DispyModule class
#Dispyのコマンドモジュールクラス．
class DModule(MModule):
    Disbot:discord.Client = None
    msg:discord.Message = None

    def __init__(self) -> void:
        self.ModuleName = "dmodule"
        return

#DispyDeveloper module
#Dispyの開発者用コマンドが含まれるコマンドモジュール．
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
            "showallguilds",
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
            #dev.showallguilds()
            result += "----------Guilds----------" + "\n"
            for server in data.client.guilds:
                result += server.name + " ID:" + str(server.id) + "\n"
            result += "----------End----------" + "\n"
        elif args[1] == self.Commands[6]:
            #dev.help()
            result = self.ShowHelp()
        return result

#DispyData class
#Dispyのサーバー情報を格納するデータクラス．
class DData(object):
    Server_Name:str = "server"
    Server_Id:int = 0
    Server_DefaultChannel_Id:int = 0

    def __init__(self,SName:str,SId:int,SChannelId:int) -> void:
        self.Server_Name = SName
        self.Server_Id = SId
        self.Server_DefaultChannel_Id = SChannelId
        return

    #データを辞書型に変換して返します．
    def ToDict(self) -> dict:
        dc:dict = {"Server_Name":self.Server_Name,
              "Server_Id":self.Server_Id,
              "Server_DefaultChannel_Id":self.Server_DefaultChannel_Id
              }
        return dc

    #未定義
    def ToJSON(self) -> bool:
        return True

#'M'inamin's'Dis'cordbotOn'Py'thon class
#discordボットでコマンド機能を提供する為のコマンドクラス．
class MDispy(MCommand):
    #ユーザから送信されたメッセージ情報．
    msg:discord.Message = None
    #ボットが所属しているサーバー情報
    Datas:List[DData] = []
    def __init__(self) -> void:
        super().__init__()
        client = discord.Client()
        return

    #メッセージ情報を登録します．
    def SetMsg(self,newmsg:discord.Message):
        self.msg = newmsg
        for module in self.Modules:
            if isinstance(module,DModule):
                module.msg = newmsg
        return

#DataControl　データを操作するための関数
    #サーバIDからデータを検索します．合致したサーバ情報を返します．
    def Search(self,SId:int) -> DData:
        for data in self.Datas:
            if data.Server_Id == Sid:
                return data
        return None

    #新たにサーバ情報を新規追加します．
    def AddNewData(self,newSName:str,newSId:int,newSChannelId:int) -> bool:
        for data in self.Datas:
            if data.Server_Id == data:
                return False
        newdata = DData(newSName,newSId,newSChannelId)
        self.Datas.append(newdata)
        return True

    #指定したサーバIDの出力チャンネルを指定したチャンネルIDに設定します．
    def SetNewData(self,TargetSId:int,newSChId:int) -> bool:
        for data in self.Datas:
            if data.Server_Id == TargetSId:
                data.Server_DefaultChannel_Id = newSChId
                return True
        return False

    #JSONファイルからサーバ情報を取得し，データリストに格納します．
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

    #データをJSON形式で保存します．
    def Save(self,path:str) -> bool:
        datas:dict = {}
        idx:int = 0
        for data in self.Datas:
            datas[str(idx)] = data.ToDict()
            idx += 1
        with open(path,"w") as f:
            json.dump(datas,f,ensure_ascii=False)
        return True

    #初期化用にボットが所属しているサーバを取得し，規定のチャンネルに出力させます．
    #規定では先頭にある「テキストチャンネル」に設定されます．
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