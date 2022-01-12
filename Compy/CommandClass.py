class MCommand():
    Modules : List[MModule]
    SprtInArg : str = ','
    ModSprt : str = '.'

    def IncludeModule(self,module:MModule):
        self.Modules.append(module)

    def ExecuteCommand(self,cmd:str):
        pass
    
    def EncodeWords(self,word:str):
        level : int = 0
        args : List[str] = []
        #std.print("aaa")
        args.append('')
        for w in word:
            if w == self.ModSprt:
                level = level + 1
                continue
            elif w == '(' || w == ')':
                level = level + 1
                continue
            elif w == self.SprtInArg:
                level = level + 1
                continue
            args[level] = args[level] + w

        return args



class MModule():
    Name : str = "module"

    def ExecuteCommand(self,cmd : str,args : List[str]):
        for arg in args:
            if cmd == ''

class Std(MModule):
    Name = "std"

    def ExecuteCommand(self,args: List[str]):
        cmd : str = args[1]
        if cmd == 'print':
            print(args[2])
        elif cmd == 'help'