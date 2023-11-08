"""This module contains the 'rm' command class."""

from os import remove, path as os_path
from shutil import rmtree
from utils import TextTools, Error
from commands._base import Command


class Rm(Command):
    """Class for the 'rm' command. Removes a file or directory."""

    @staticmethod
    def main(path):
        """Removes a file or directory."""

        error = False
        pth = TextTools.path(path[0]) if len(path) > 0 else ""

        if len(path) != 1:
            error = Error.generic(
                "invalidArguments", {"expected": "1", "actual": len(path)}
            )
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
