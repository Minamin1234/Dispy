class MCommand():
    Modules : List[]
    Sprt : str = ' '
    ModSprt : str = '.'

    def ExecuteCommand(self,cmd:str):
        pass
    
    def EncodeWords(self,word:str):
        level : int = 0
        args : List[str] = []
        modFrag : bool = False

        args.append('')
        for w in word:
            if w == self.ModSprt:
                modFrag = True
            elif modFrag == True && level == 0:
                args[0] = args[0] + w

            if w == self.Sprt && level != 0:
                level = level + 1
            elif w == ''

        pass


class MModule():
    Name : str = "module"

    def ExecuteCommand(self,cmd : str,args : List[str]):
        for arg in args:
            if cmd == ''

class Std(MModule):
    Name = "std"

    def ExecuteCommand(self, cmd: str, args: List[str]):
        for arg in args:
            if cmd == 'print'