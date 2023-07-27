"""This module contains all the commands that can be run in the shell and their functions."""
from os import listdir, remove, makedirs, chdir, path as os_path, rename as os_rename
from shutil import rmtree, copytree, copy
from tabulate import tabulate
from submodules import Config, TextTools, Error

class Commands:
    """This class contains all the commands that can be run in the shell."""
    list = Config.data["commands"]
    
    @staticmethod
    def find(command):
        """Returns the name of the command if it exists, False otherwise."""
        for cmd in Commands.list:
            if (cmd == command): return cmd
            for alias in Commands.list[cmd]["aliases"]:
                if (alias == command): return cmd
        return False
    
    @staticmethod
    def run(command):
        """Returns the function of the command if it exists, False otherwise."""
        if (command=="exit"): return lambda args: exit(0)

        cmd = Commands.find(command)

        if (cmd == False): return False
        return getattr(Commands, cmd)

    @staticmethod
    def help(*args):
        """Displays the help message."""

        if (len(Commands.list) == 0):
            print("No commands found")
            return 0
        TextTools.print("\n/commands in brackets are other aliases for the command/\n", "magenta")
        for command in Commands.list:
            TextTools.printCommand(command, Commands.list[command])
        print("")

    @staticmethod
    def dir(*args):
        """Displays the content of the current directory."""
        dirs = listdir()
        data = []
        for dir in dirs:
            info = {
                "name": dir,
                "size": str(os_path.getsize("./"+dir))+" BYTES",
                "type": ("<DIR>" if os_path.isdir("./"+dir) else "<FILE>")
            }
            data.append(info.values())
            # print("{name}\t{type}\t{size}".format(**info))
        print(tabulate(data, headers=["Name", "Size", "Type"], tablefmt="grid"))
    
    
    @staticmethod
    def rename(path):
        """Renames a file or directory."""
        error = False
        pth = TextTools.paths(*path)

        if (len(path) != 2):
            error = Error.generic("invalidArguments", {"expected": "2", "actual": len(path)})
        elif (not os_path.exists(pth[0])):
            error = Error.command("rename", "notFound")
        elif (os_path.exists(pth[1])):
            error = Error.command("rename", "alreadyExists")

        if (error):
            Error.display(error)
            return 1
        
        os_rename(pth[0], pth[1])

        print("")

    @staticmethod
    def cd(path):
        """Changes the current directory."""
        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if (len(path) != 1):
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif (not os_path.exists(pth)): 
            error = Error.command("cd", "notFound")
        elif (not os_path.isdir(pth)): 
            error = Error.command("cd", "notDirectory")

        if (error): 
            Error.display(error)
            return 1
        
        chdir(pth)

    @staticmethod
    def md(path):
        """Creates a directory."""
        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if (len(path) != 1):
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif (os_path.exists(pth)):
            error = Error.command("md", "alreadyExists")

        if (error): 
            Error.display(error)
            return 1

        makedirs(pth) 
        print("")

    @staticmethod
    def cp(path):
        """Copies a file or directory."""
        error = False
        pth = TextTools.paths(*path)

        if (len(path) != 2):
            error = Error.generic("invalidArguments", {"expected": "2", "actual": len(path)})
        elif(not os_path.exists(pth[0])):
            error = Error.command("cp", "notFound")
        elif (os_path.exists(pth[1])):
            error = Error.command("cp", "alreadyExists")

        if (error):
            Error.display(error)
            return 1

        if (not os_path.isdir(pth[0])):
            copy(pth[0], pth[1])
        
        copytree(pth[0], pth[1])
        print("")

    @staticmethod
    def rm(path):
        """Removes a file or directory."""
        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if (len(path) != 1):
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif (not os_path.exists(pth)):
            error = Error.command("rm", "notFound")

        if (error):
            Error.display(error)
            return 1
        
        if (os_path.isdir(pth)): rmtree(pth)
        else: remove(pth)
        print("")
