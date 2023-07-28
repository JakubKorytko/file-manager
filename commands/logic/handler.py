"""Handles commands. Runs them if they exist."""

from sys import exit as sys_exit
from commands import Command
from commands.logic.load import config

class CommandsHandler:
    """Class that handles commands."""

    @staticmethod
    def _verify():
        """Verifies that the number of commands matches the number of command classes."""

        commands = config.data["commands"]
        subclasses = Command.__subclasses__()

        if len(subclasses) != len(commands):
            print("Number of commands does not match the number of command classes")
            print("Fix it by adding/removing a command class", end=" ")
            print("or adding/removing a command in the config file")
            print("Exiting...")
            exit(1)

        subclasses_names = [subclass.__name__.lower() for subclass in subclasses]

        for command in commands:
            if command not in subclasses_names:
                print(f"Command '{command}' not found in commands directory")
                print("Fix it by adding/removing a command class", end=" ")
                print("or adding/removing a command in the config file")
                print("Exiting...")
                exit(1)

    @staticmethod
    def _convert_if_alias(command):
        """Converts a command to its name if it is an alias."""

        commands = config.data["commands"]

        for cmd in commands:
            if cmd == command:
                return cmd
            for alias in commands[cmd]["aliases"]:
                if alias == command:
                    return cmd

        return command

    @staticmethod
    def run(command):
        """Runs a command if it exists."""

        if command=="exit":
            return lambda args: sys_exit(0)
            # args are needed for proper function call even if they are not used

        CommandsHandler._verify()

        command_name = CommandsHandler._convert_if_alias(command)

        subclasses = Command.__subclasses__()

        for subclass in subclasses:
            if command_name == subclass.__name__.lower():
                return subclass.main

        return False
