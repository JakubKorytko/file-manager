from shutil import copytree, copy
from os import path as os_path
from submodules import TextTools, Error
from commands.command import Command

class Main(Command):

    @staticmethod
    def main(path):
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