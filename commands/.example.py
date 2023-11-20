"""This is example code for your own commands class. It is not used by the program."""

from commands._base import Command

# | Class needs to inherit from the Command class.
# | If it doesn't, it won't be loaded by the program.

# from files_manager.src.utils import TextTools, Error
# | These are the utils modules you will most likely need.
# | You can read more about them in the utils folder
# | (look at the docstrings).

# | If you need the list of commands, you can import it like this:
# from files_manager.src.logic.load import config

# | To access the list, use:
# config.data["commands"]

# | DON'T MODIFY THE LIST, IT WILL BREAK THE PROGRAM.
# | The only purpose of this list is
# | to for example display all commands in the help message.

# | You can read more about it in the logic folder
# | (look at the docstrings).


class Example(Command):
    """Class for the 'help' command. Displays the help message."""

    # The function that will be called when the command is executed.
    # It needs to be static,
    # so it can be called without an instance of the class.
    # It also needs to have the main name,
    # so it can be called by the CommandsHandler class.
    # You can specify other methods, but they won't be called by the program.
    @staticmethod
    def main(
        *args,
    ):  # You can specify any number of arguments here, *args is just an example.
        """This is the main method of the command. It is called when the command is executed."""

        Command.no_args(args, "example")
        # If you are not using any arguments,
        # use this method at the start of the main method.

        # The first argument is the arguments list,
        # the second is the name of the command.
        # The second argument is the name of the command,
        # it is used in the info message.

        # The only purpose of this method is to display a message
        # that the arguments will be ignored.
        # It will not stop the program.

        # The main method should return a positive integer
        # if the command was successful.
        return 1
