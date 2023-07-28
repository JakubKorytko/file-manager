
from commands.command import Command
from commands.load import Config

class CommandsHandler:

    def __verify(self):
        commands = Config.data["commands"]
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

    @property
    def commands_list(self):
        """Returns the list of commands."""
        self.__verify()

        return Config.data["commands"]

    def __convertIfAlias(self, command):
        commands = Config.data["commands"]

        for cmd in commands:
            if cmd == command:
                return cmd
            for alias in commands[cmd]["aliases"]:
                if alias == command:
                    return cmd

        return command


    def run(self, command, *args):
        """Runs a command if it exists."""
        self.__verify()

        command_name = self.__convertIfAlias(command)

        subclasses = Command.__subclasses__()

        for subclass in subclasses:
            if command_name == subclass.__name__.lower():
                subclass.main(*args)
                return True

        return False

CommandsHandler = CommandsHandler()
