from typing import NoReturn as void
from typing import List
from Compy import MCommand
import discord

class MDispy(MCommand):
    msg:discord.Message = None

    def __init__(self) -> void:
        super().__init__()
        return

    def SetMsg(self,message:discord.Message) -> void:
        self.msg = message
        return

    async def PrintString(self,value) -> void:
        super().PrintString(value)
        await self.msg.channel.send(str(value))
        return

        





