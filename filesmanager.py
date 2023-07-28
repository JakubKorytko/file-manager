"""Main module of the program, contains the main loop and the main function."""
from colorama import init as colorama_init
from submodules import TextTools, Error
from commands import Commands

class FilesManager:
    """Main class of the program."""

    @staticmethod
    def start():
        """Starts the program."""
        FilesManager.init()
        FilesManager.loop()

    @staticmethod
    def init():
        """Initializes the program."""
        colorama_init()
        TextTools.print('\nFile manager (use "exit" to exit, "help" to list commands)\n', "magenta")

    @staticmethod
    def run(cmnd):
        """Runs a command."""
        args = TextTools.scrap_args(cmnd)

        if len(args) == 0:
            return 1

        command = args[0]

        command_function = Commands.run(command)

        if command_function is False:
            error = Error.generic("unknownCommand", {"command": command})
            Error.display(error)
            return 1

        command_function(args[1:])
        return 1

    @staticmethod
    def loop():
        """Main loop of the program."""

        while FilesManager.run(input(TextTools.indicator())):
            pass
