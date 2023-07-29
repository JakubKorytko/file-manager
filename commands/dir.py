"""This module contains the 'dir' command class."""

from os import listdir, path as os_path
from tabulate import tabulate
from commands import Command

class Dir(Command):
    """Class for the 'dir' command. Displays the content of the current directory."""

    @staticmethod
    def main(*args):
        """Displays the content of the current directory."""

        Dir.no_args(args, "dir")

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
