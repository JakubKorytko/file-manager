"""This module contains the 'help' command class."""

from utils import TextTools
from commands import Command
from commands.logic.load import Config

class Help(Command):
    """Class for the 'help' command. Displays the help message."""

    @staticmethod
    def main(*args):
        """Displays the help message."""

        Command.no_args(args, "help")

        if len(Config.data["commands"]) == 0:
            print("No commands found")
            return 1

        TextTools.print("\n/commands in brackets are other aliases for the command/\n", "magenta")
        for command in Config.data["commands"]:
            TextTools.print_command(command, Config.data["commands"][command])

        print("")
        return 1
