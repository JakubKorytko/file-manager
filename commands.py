from submodules import *
from tabulate import tabulate
import shutil
import os

class Commands:

    list = data["commands"]
    
    @staticmethod
    def find(command):
        for cmd in Commands.list:
            if (cmd == command): return cmd
            for alias in Commands.list[cmd]["aliases"]:
                if (alias == command): return cmd
        return False
    
    @staticmethod
    def run(command):

        if (command=="exit"): return lambda args: exit(0)

        cmd = Commands.find(command)

        if (cmd == False): return False
        return getattr(Commands, cmd)

    @staticmethod
    def help(*args):
        if (len(Commands.list) == 0):
            print("No commands found")
            return 0
        TextTools.print("\n/commands in brackets are other aliases for the command/\n", "magenta")
        for command in Commands.list:
            TextTools.printCommand(command, Commands.list[command])
        print("")

    @staticmethod
    def dir(*args):
        dirs = os.listdir()
        data = []
        for dir in dirs:
            info = {
                "name": dir,
                "size": str(os.path.getsize("./"+dir))+" BYTES",
                "type": ("<DIR>" if os.path.isdir("./"+dir) else "<FILE>")
            }
            data.append(info.values())
            # print("{name}\t{type}\t{size}".format(**info))
        print(tabulate(data, headers=["Name", "Size", "Type"], tablefmt="grid"))
    
    
    @staticmethod
    def rename(path):
        error = False
        pth = TextTools.paths(*path)

        if (len(path) != 2):
            error = Error.generic("invalidArguments", {"expected": "2", "actual": len(path)})
        elif (not os.path.exists(pth[0])):
            error = Error.command("rename", "notFound")
        elif (os.path.exists(pth[1])):
            error = Error.command("rename", "alreadyExists")

        if (error):
            Error.display(error)
            return 1
        
        os.rename(pth[0], pth[1])

        print("")

    @staticmethod
    def cd(path):
        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if (len(path) != 1):
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif (not os.path.exists(pth)): 
            error = Error.command("cd", "notFound")
        elif (not os.path.isdir(pth)): 
            error = Error.command("cd", "notDirectory")

        if (error): 
            Error.display(error)
            return 1
        
        os.chdir(pth)

    @staticmethod
    def md(path):
        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if (len(path) != 1):
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif (os.path.exists(pth)):
            error = Error.command("md", "alreadyExists")

        if (error): 
            Error.display(error)
            return 1

        os.makedirs(pth) 
        print("")

    @staticmethod
    def cp(path):
        error = False
        pth = TextTools.paths(*path)

        if (len(path) != 2):
            error = Error.generic("invalidArguments", {"expected": "2", "actual": len(path)})
        elif(not os.path.exists(pth[0])):
            error = Error.command("cp", "notFound")
        elif (os.path.exists(pth[1])):
            error = Error.command("cp", "alreadyExists")

        if (error):
            Error.display(error)
            return 1

        if (not os.path.isdir(pth[0])):
            shutil.copy(pth[0], pth[1])
        
        shutil.copytree(pth[0], pth[1])
        print("")

    @staticmethod
    def rm(path):
        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if (len(path) != 1):
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif (not os.path.exists(pth)):
            error = Error.command("rm", "notFound")

        if (error):
            Error.display(error)
            return 1
        
        if (os.path.isdir(pth)): shutil.rmtree(pth)
        else: os.remove(pth)
        print("")