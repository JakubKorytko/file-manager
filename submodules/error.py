"""This module contains the Error class, which is used to display error messages."""
from submodules.utils import TextTools, Config

class Error:

    commands = Config.data["commands"]
    genericCodes = Config.data["genericErrorCodes"]

    @staticmethod
    def generic(code, args={}):
        """Returns a generic error message."""
        return Error.genericCodes[code].format(**args)

    @staticmethod
    def command(command, code, args={}):
        """Returns a command error message."""
        return Error.commands[command]["errorCodes"][code].format(**args)
    
    @staticmethod
    def display(error):
        """Displays an error message."""
        TextTools.print(error, "red")