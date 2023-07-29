"""This module contains the Error class, which is used to display error messages."""
from . import TextTools

class Error:
    """This class is used to display error messages."""

    data_loaded = False

    # Its a false positive, data property is dynamically set by the Config class

    @staticmethod
    def not_loaded_message(function_name):
        """Returns an error message when the data is not loaded."""

        error_message = ("Error: Error data not loaded.",
        f"Please run Error.set_data() before using Error.{function_name}()")
        return error_message

    @staticmethod
    def set_data(data):
        """Sets commands and generic_codes properties."""

        Error.commands = data["commands"]
        Error.generic_codes = data["genericErrorCodes"]
        Error.data_loaded = True

    @staticmethod
    def unset_data():
        """Unsets commands and generic_codes properties."""

        Error.commands = None
        Error.generic_codes = None
        Error.data_loaded = False

    @staticmethod
    def generic(code, args=None):
        """Returns a generic error message."""

        # The error messages you can run are stored in the "genericErrorCodes"
        # property (by default in the "config.json" file)

        # To avoid W0102 (dangerous default value {} as argument)
        if args is None:
            args = {}

        if not Error.data_loaded:
            return Error.not_loaded_message("generic")

        return Error.generic_codes[code].format(**args)

    @staticmethod
    def command(command, code, args=None):
        """Returns a command error message."""

        # The error messages you can run are stored in the "errorCodes" property of the command
        # By default in the "config.json" file
        # Run it like this: Error.command("command", "errorCode", {"arg": "value"})

        # To avoid W0102 (dangerous default value {} as argument)
        if args is None:
            args = {}

        if not Error.data_loaded:
            return Error.not_loaded_message("command")

        return Error.commands[command]["errorCodes"][code].format(**args)

    @staticmethod
    def display(error):
        """Displays an error message."""

        TextTools.print(error, "red")
