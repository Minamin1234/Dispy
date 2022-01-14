from typing import NoReturn as void

class MCommand:
    Modules:str = []
    SprtModule:str = "."
    SprtInArg:str = ","

    def __init__(self) -> void:
        pass

    def IncludeModule(self,module:MModule) -> void:
        pass

    def ExecuteCommand(self,cmd:str) -> void:
        level:int = 0
        args:str = [""]
        for w in cmd:
            if w == self.SprtModule:
                level = level + 1
                args.append("")
                continue
            elif w == self.SprtInArg:
                level = level + 1
                args.append("")
                continue
            args[level] = args[level] + w
        
        for module in self.Modules:
            if args[0] == module.ModuleName:
                module.ExecuteCommand(args)
        return

class MModule:
    ModuleName:str = "module"

    def __init__(self) -> void:
        pass

    def ExecuteCommand(self,args:str) -> bool:
        pass

class MStd(MModule):
    def __init_subclass__(cls) -> void:
        super(MStd,self).__init_subclass__()
        self.ModuleName = "std"

