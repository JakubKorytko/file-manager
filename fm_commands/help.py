"""This module contains the 'help' command class."""

from file_manager.src.logic import config
from file_manager.src.utils import TextTools
from fm_commands._base import Command


class Help(Command):
    """Class for the 'help' command. Displays the help message."""

    @staticmethod
    def main(*args):
        """Displays the help message."""

        Command.no_args(args, "help")

        if len(config.data["commands"]) == 0:
            print("No commands found")
            return 1

        TextTools.print(
            "\n/commands in brackets are other aliases for the command/\n", "magenta"
        )
        for command in config.data["commands"]:
            TextTools.print_command(command, config.data["commands"][command])

        print("")

        TextTools.print_command(
            "exit", {"description": "exit the program", "aliases": []}
        )

        print("")
        return 1
