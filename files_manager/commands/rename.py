"""This module contains the 'rename' command class."""

from os import path as os_path
from os import rename as os_rename

from files_manager.commands._base import Command
from files_manager.src import Error, TextTools


class Rename(Command):
    """Class for the 'rename' command. Renames a file or directory."""

    @staticmethod
    def main(path):
        """Renames a file or directory."""

        error = False
        pth = TextTools.paths(*path)

        if len(path) != 2:
            error = Error.generic(
                "invalidArguments", {"expected": "2", "actual": len(path)}
            )
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
