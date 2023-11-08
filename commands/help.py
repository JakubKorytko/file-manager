"""This module contains the 'help' command class."""

from utils import TextTools
from commands._base import Command
from logic.load import config


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
        return 1
