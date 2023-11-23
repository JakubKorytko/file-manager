"""Main module of the program, contains the main loop and the main function."""
from os import path

from colorama import init as colorama_init

from files_manager.src.logic import CommandsHandler, config
from files_manager.src.utils import Error, TextTools
from fm_commands._base import Command


class FilesManager:
    """Main class of the program."""

    @staticmethod
    def start(script_dir):
        """Starts the program."""
        FilesManager.set_config_path(script_dir)
        FilesManager.init()
        FilesManager.loop()

    @staticmethod
    def set_config_path(script_dir):
        """Sets the path to the config file."""

        txt_path = "fm_config.json"
        txt_parent_path = f"../{txt_path}"

        file = path.join(script_dir, txt_path)
        parent_file = path.join(script_dir, txt_parent_path)

        if path.isfile(parent_file):
            config.data_path = parent_file
        else:
            config.data_path = file

    @staticmethod
    def init():
        """Initializes the program."""
        colorama_init()
        TextTools.print(
            '\nFile manager (use "exit" to exit, "help" to list commands)\n', "magenta"
        )

    @staticmethod
    def run(cmnd):
        """Runs a command."""
        args = TextTools.scrap_args(cmnd)

        if len(args) == 0:
            return 1

        command = args[0]

        command_function = CommandsHandler.run(command)

        if command_function is False:
            error = Error.generic("unknownCommand", {"command": command})
            Error.display(error)
            return 1

        command_function(args[1:])
        return 1

    @staticmethod
    def loop():
        """Main loop of the program."""
        Error.set_data(config.data)
        CommandsHandler.set_data(config.data, Command.__subclasses__())

        while FilesManager.run(input(TextTools.indicator())):
            pass
