"""This module contains the Error class, which is used to display error messages."""
from submodules.utils import TextTools, Config

class Error:
    """This class is used to display error messages."""

    commands = Config.data["commands"] #pylint: disable=E1136
    genericCodes = Config.data["genericErrorCodes"] #pylint: disable=E1136
    # Its a false positive, data property is dynamically set by the Config class

    @staticmethod
    def generic(code, args=None):
        """Returns a generic error message."""

        # To avoid W0102 (dangerous default value {} as argument)
        if args is None:
            args = {}

        return Error.genericCodes[code].format(**args)

    @staticmethod
    def command(command, code, args=None):
        """Returns a command error message."""

        # To avoid W0102 (dangerous default value {} as argument)
        if args is None:
            args = {}

        return Error.commands[command]["errorCodes"][code].format(**args)

    @staticmethod
    def display(error):
        """Displays an error message."""

        TextTools.print(error, "red")
