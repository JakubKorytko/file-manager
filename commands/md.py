"""This module contains the 'md' command class."""

from os import makedirs
from os import path as os_path

from commands._base import Command
from files_manager.src.utils import Error, TextTools


class Md(Command):
    """Class for the 'md' command. Creates a directory."""

    @staticmethod
    def main(path):
        """Creates a directory."""

        error = False
        dir_path = TextTools.path(path[0]) if len(path) > 0 else ""

        if len(path) != 1:
            error = Error.generic(
                "invalidArguments", {"expected": "1", "actual": len(path)}
            )
        elif os_path.exists(dir_path):
            error = Error.command("md", "alreadyExists")

        if error:
            Error.display(error)
            return 1

        makedirs(dir_path)
        print("")
        return 1
