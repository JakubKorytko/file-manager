"""This module contains the 'cd' command class."""

from os import chdir, path as os_path
from commands.command import Command
from submodules import TextTools, Error

class Cd(Command):
    """Class for the 'cd' command. Changes the current directory."""

    @staticmethod
    def main(path):
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