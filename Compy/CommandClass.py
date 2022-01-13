class MCommand():
    Modules : List[MModule]
    SprtInArg : str = ','
    ModSprt : str = '.'

    def __init__(self):
        newmod = Std()
        self.IncludeModule(newmod)

    def IncludeModule(self,module:MModule):
        self.Modules.append(module)

    def ExecuteCommand(self,cmd:str):
        args : List[str] = self.EncodeWords(cmd)
        for mod in self.Modules:
            if mod.Name == args[0]:
                mod.ExecuteCommand(self,cmd : str,args : List[str]):
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
    Commands : List[str]

    def AddCommand(self,cmd : str):
        self.Commands.append(cmd)

    def ExecuteCommand(self,cmd : str,args : List[str]):
        for arg in args:
            if cmd == ''

class Std(MModule):
    Name = "std"

    def __init__(self):
        pass

    def ExecuteCommand(self,args: List[str]):
        cmd : str = args[1]
        if cmd == 'print':
            print(args[2])
        elif cmd == 'help':
            print('a')