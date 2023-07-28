"""This is the base module for all the commands."""

class Command:
    """Base class for all the commands."""

    # list = Config.data["commands"] #pylint: disable=E1136
    # # Its a false positive, data property is dynamically set by the Config class

    @staticmethod
    def no_args(args, command):
        """Prints an info message if the command is called with arguments when it shouldn't be."""

        if len(args[0]) > 0:
            print(f"'{command}' command does not take any arguments, ignoring them...")