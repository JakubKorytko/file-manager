"""This module contains all the commands that can be run in the shell and their functions."""
# from sys import exit as sys_exit

class Command:
    """This class contains all the commands that can be run in the shell."""

    # list = Config.data["commands"] #pylint: disable=E1136
    # # Its a false positive, data property is dynamically set by the Config class

    @staticmethod
    def no_args(args, command):
        """Prints an info message if the command is called with arguments when it shouldn't be."""

        if len(args[0]) > 0:
            print(f"'{command}' command does not take any arguments, ignoring them...")

    # @staticmethod
    # def find(command):
    #     """Returns the name of the command if it exists, False otherwise."""

    #     for cmd in Command.list:
    #         if cmd == command:
    #             return cmd
    #         for alias in Command.list[cmd]["aliases"]:
    #             if alias == command:
    #                 return cmd
    #     return False

    # @staticmethod
    # def run(command):
    #     """Returns the function of the command if it exists, False otherwise."""

    #     if command=="exit":
    #         return lambda: sys_exit(0)

    #     cmd = Command.find(command)

    #     if cmd is False:
    #         return False

    #     return getattr(Command, cmd)
