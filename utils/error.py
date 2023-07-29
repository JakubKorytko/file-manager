"""This module contains the Error class, which is used to display error messages."""
from . import TextTools

class Error:
    """This class is used to display error messages."""

    data_loaded = False

    # Its a false positive, data property is dynamically set by the Config class

    @staticmethod
    def set_data(data):
        """Sets commands and generic_codes properties."""

        Error.commands = data["commands"]
        Error.generic_codes = data["genericErrorCodes"]
        Error.data_loaded = True

    @staticmethod
    def generic(code, args=None):
        """Returns a generic error message."""

        # To avoid W0102 (dangerous default value {} as argument)
        if args is None:
            args = {}

        if not Error.data_loaded:
            return ("Error: Error data not loaded.",
            "Please run Error.set_data() before using Error.generic()")

        return Error.generic_codes[code].format(**args)

    @staticmethod
    def command(command, code, args=None):
        """Returns a command error message."""

        # To avoid W0102 (dangerous default value {} as argument)
        if args is None:
            args = {}

        if not Error.data_loaded:
            return ("Error: Error data not loaded.",
            "Please run Error.set_data() before using Error.command()")

        return Error.commands[command]["errorCodes"][code].format(**args)

    @staticmethod
    def display(error):
        """Displays an error message."""

        TextTools.print(error, "red")
