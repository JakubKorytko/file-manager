"""This module contains all the commands that can be run in the shell and their functions."""
from os import listdir, remove, makedirs, chdir, path as os_path, rename as os_rename
from shutil import rmtree, copytree, copy
from sys import exit as sys_exit
from tabulate import tabulate
from submodules import Config, TextTools, Error

class Commands:
    """This class contains all the commands that can be run in the shell."""

    list = Config.data["commands"] #pylint: disable=E1136
    # Its a false positive, data property is dynamically set by the Config class

    @staticmethod
    def no_args(args, command):
        """Prints an info message if the command is called with arguments when it shouldn't be."""

        if len(args[0]) > 0:
            print(f"'{command}' command does not take any arguments, ignoring them...")

    @staticmethod
    def find(command):
        """Returns the name of the command if it exists, False otherwise."""

        for cmd in Commands.list:
            if cmd == command:
                return cmd
            for alias in Commands.list[cmd]["aliases"]:
                if alias == command:
                    return cmd
        return False

    @staticmethod
    def run(command):
        """Returns the function of the command if it exists, False otherwise."""

        if command=="exit":
            return lambda: sys_exit(0)

        cmd = Commands.find(command)

        if cmd is False:
            return False

        return getattr(Commands, cmd)

    @staticmethod
    def help(*args):
        """Displays the help message."""

        Commands.no_args(args, "help")

        if len(Commands.list) == 0:
            print("No commands found")
            return 1

        TextTools.print("\n/commands in brackets are other aliases for the command/\n", "magenta")
        for command in Commands.list:
            TextTools.print_command(command, Commands.list[command])

        print("")
        return 1

    @staticmethod
    def dir(*args):
        """Displays the content of the current directory."""

        Commands.no_args(args, "dir")

        dirs = listdir()
        data = []

        for directory in dirs:
            info = {
                "name": directory,
                "size": str(os_path.getsize("./"+directory))+" BYTES",
                "type": ("<DIR>" if os_path.isdir("./"+directory) else "<FILE>")
            }
            data.append(info.values())

        print(tabulate(data, headers=["Name", "Size", "Type"], tablefmt="grid"))
        return 1


    @staticmethod
    def rename(path):
        """Renames a file or directory."""

        error = False
        pth = TextTools.paths(*path)

        if len(path) != 2:
            error = Error.generic("invalidArguments", {"expected": "2", "actual": len(path)})
        elif not os_path.exists(pth[0]):
            error = Error.command("rename", "notFound")
        elif os_path.exists(pth[1]):
            error = Error.command("rename", "alreadyExists")

        if error:
            Error.display(error)
            return 1

        os_rename(pth[0], pth[1])
        print("")
        return 1

    @staticmethod
    def cd(path):
        """Changes the current directory."""

        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if len(path) != 1:
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif not os_path.exists(pth): 
            error = Error.command("cd", "notFound")
        elif not os_path.isdir(pth): 
            error = Error.command("cd", "notDirectory")

        if error:
            Error.display(error)
            return 1

        chdir(pth)
        return 1

    @staticmethod
    def md(path):
        """Creates a directory."""

        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if len(path) != 1:
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif os_path.exists(pth):
            error = Error.command("md", "alreadyExists")

        if error:
            Error.display(error)
            return 1

        makedirs(pth)
        print("")
        return 1

    @staticmethod
    def cp(path):
        """Copies a file or directory."""

        error = False
        pth = TextTools.paths(*path)

        if len(path) != 2:
            error = Error.generic("invalidArguments", {"expected": "2", "actual": len(path)})
        elif not os_path.exists(pth[0]):
            error = Error.command("cp", "notFound")
        elif os_path.exists(pth[1]):
            error = Error.command("cp", "alreadyExists")

        if error:
            Error.display(error)
            return 1

        if not os_path.isdir(pth[0]):
            copy(pth[0], pth[1])

        copytree(pth[0], pth[1])
        print("")
        return 1

    @staticmethod
    def rm(path):
        """Removes a file or directory."""

        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if len(path) != 1:
            error = Error.generic("invalidArguments", {"expected": "1", "actual": len(path)})
        elif not os_path.exists(pth):
            error = Error.command("rm", "notFound")

        if error:
            Error.display(error)
            return 1

        if os_path.isdir(pth):
            rmtree(pth)
        else:
            remove(pth)

        print("")
        return 1
