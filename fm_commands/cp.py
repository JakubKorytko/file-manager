"""This module contains the 'cp' command class."""

from os import path as os_path
from shutil import copy, copytree

from files_manager.src.utils import Error, TextTools
from fm_commands._base import Command


class Cp(Command):
    """Class for the 'cp' command. Copies a file or directory."""

    @staticmethod
    def main(path):
        """Copies a file or directory."""

        error = False
        paths = TextTools.paths(*path)

        if len(path) != 2:
            error = Error.generic(
                "invalidArguments", {"expected": "2", "actual": len(path)}
            )

        if not error:
            [source, destination] = paths

        if not error and not os_path.exists(source):
            error = Error.command("cp", "notFound")

        if not error and os_path.exists(destination):
            error = Error.command("cp", "alreadyExists")

        if error:
            Error.display(error)
            return 1

        if os_path.isdir(source):
            copytree(source, destination)
        else:
            copy(source, destination)

        print("")
        return 1
