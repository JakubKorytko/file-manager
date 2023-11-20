"""This module contains the 'cd' command class."""

from os import chdir
from os import path as os_path

from files_manager.commands._base import Command
from files_manager.src import Error, TextTools


class Cd(Command):
    """Class for the 'cd' command. Changes the current directory."""

    @staticmethod
    def main(path):
        """Changes the current directory."""

        error = False

        if len(path) != 1:
            error = Error.generic(
                "invalidArguments", {"expected": "1", "actual": len(path)}
            )

        if not error:
            pth = TextTools.path(path[0])

        if not error and not os_path.exists(pth):
            error = Error.command("cd", "notFound")

        if not error and not os_path.isdir(pth):
            error = Error.command("cd", "notDirectory")

        if error:
            Error.display(error)
            return 1

        chdir(pth)
        return 1
