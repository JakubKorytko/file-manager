"""This module contains the 'md' command class."""

from os import makedirs
from os import path as os_path

from commands._base import Command
from utils import Error, TextTools


class Md(Command):
    """Class for the 'md' command. Creates a directory."""

    @staticmethod
    def main(path):
        """Creates a directory."""

        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if len(path) != 1:
            error = Error.generic(
                "invalidArguments", {"expected": "1", "actual": len(path)}
            )
        elif os_path.exists(pth):
            error = Error.command("md", "alreadyExists")

        if error:
            Error.display(error)
            return 1

        makedirs(pth)
        print("")
        return 1
