from typing import NoReturn as void
from typing import List
from Compy import Compy.MCommand
import discord

class Dispy(MCommand):
    msg:discord.Message = None

    def SetMsg(self,message:discord.Message):
        self.msg = message

    async def PrintString(self,value):
        super().PrintString(value)
        await self.msg.channel.send(str(value))

        





