"""This module contains the 'help' command class."""

from submodules import TextTools
from commands.command import Command

class Help(Command):
    """Class for the 'help' command. Displays the help message."""

    @staticmethod
    def main(*args):
        """Displays the help message."""

        Command.no_args(args, "help")

        if len(Command.list) == 0:
            print("No commands found")
            return 1

        TextTools.print("\n/commands in brackets are other aliases for the command/\n", "magenta")
        for command in Command.list:
            TextTools.print_command(command, Command.list[command])

        print("")
        return 1
