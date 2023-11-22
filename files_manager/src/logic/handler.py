"""Handles commands. Runs them if they exist."""

from sys import exit as sys_exit


class CommandsHandler:
    """Class that handles commands."""

    data_loaded = False

    @staticmethod
    def set_data(data, classes):
        """Sets the data for the class."""

        CommandsHandler.data = data
        CommandsHandler.data_loaded = True
        CommandsHandler.classes = classes

    @staticmethod
    def wrong_data_message():
        """Prints the error message when the number of command classes
        is not equal to the number of commands and exits the program"""
        print("Fix it by adding/removing a command class", end=" ")
        print("or adding/removing a command", end=" ")
        print("in the data provided to CommandsHandler.set_data()")
        print("By default, data is fetched from the fm_config.json file")
        print("Exiting...")
        sys_exit(1)

    @staticmethod
    def _verify():
        """Verifies that the number of commands matches the number of command classes."""

        if not CommandsHandler.data_loaded:
            print("Error: CommandsHandler data not loaded.")
            print(
                "Please run CommandsHandler.set_data() before using CommandsHandler._verify()"
            )
            print("Exiting...")
            sys_exit(1)

        commands = CommandsHandler.data["commands"]
        classes = CommandsHandler.classes

        if len(classes) != len(commands):
            print("Number of commands does not match the number of command classes")
            CommandsHandler.wrong_data_message()

        class_names = [
            CommandsHandler.convert_pascal_to_snake_case(class_.__name__)
            for class_ in classes
        ]

        for command in commands:
            if command not in class_names:
                print(f"Command '{command}' not found in the commands directory")
                CommandsHandler.wrong_data_message()

    @staticmethod
    def _convert_if_alias(command):
        """Converts a command to its name if it is an alias."""

        commands = CommandsHandler.data["commands"]

        for cmd in commands:
            if cmd == command:
                return cmd
            for alias in commands[cmd]["aliases"]:
                if alias == command:
                    return cmd

        return command

    @staticmethod
    def convert_pascal_to_snake_case(name):
        """Converts a PascalCase name to snake_case."""

        first_iteration = True
        snake_case = ""

        for char in name:
            if char.isupper() and not first_iteration:
                snake_case += "_"

            snake_case += char.lower()

            if first_iteration:
                first_iteration = False

        return snake_case

    @staticmethod
    def run(command):
        """Runs a command if it exists."""

        if command == "exit":
            return lambda args: sys_exit(0)
            # args are needed for proper function call even if they are not used

        CommandsHandler._verify()

        command_name = CommandsHandler._convert_if_alias(command)

        classes = CommandsHandler.classes

        for class_ in classes:
            if command_name == CommandsHandler.convert_pascal_to_snake_case(class_.__name__):
                return class_.main

        return False
