"""This is example code for your own commands class. It is not used by the program."""

from commands import Command
# | Class needs to inherit from the Command class
# | If it doesn't, it won't be loaded by the program

# from utils import TextTools, Error
# | These are the utils modules you will most likely need

# | If you need the list of commands, you can import it like this:
# from commands.logic.load import config

# | If you are using Pylint, you should disable the C0412 warning:
# from commands.logic.load import config #pylint: disable=C0412

# | We can't group it with the other imports due to circular imports

class Example(Command):
    """Class for the 'help' command. Displays the help message."""

    # The function that will be called when the command is executed
    # It needs to be static, so it can be called without an instance of the class
    # It also needs to have the main name, so it can be called by the CommandsHandler class
    # You can specify other methods, but they won't be called by the program
    @staticmethod
    def main(*args): # You can specify any number of arguments here, *args is just an example
        """This is the main method of the command. It is called when the command is executed."""

        Command.no_args(args, "example")
        # If you are not using any arguments, use this method at the start of the main method
        # The first argument is the arguments list, the second is the name of the command
        # The second argument is the name of the command, it is used in the info message

        # The main method should return a positive integer if the command was successful
        return 1
