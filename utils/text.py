"""This module contains various tools to manipulate text."""
from os import getcwd
from re import findall as re_findall
from colorama import Fore, Style

class TextTools:
    """Class containing various tools to manipulate text."""

    @staticmethod
    def indicator():
        """Returns the colored indicator before the user input."""

        return TextTools.color(getcwd()+">", "green")

    @staticmethod
    def print_command(name, value):
        """Prints a command with its description and aliases."""

        aliases = value["aliases"]
        cmnd = name

        if len(aliases)>0:
            cmnd += " (" + ", ".join(aliases) + ")"

        formatted_name = TextTools.color(f"{cmnd}", "yellow")
        formatted_value = f"- {value['description']}"

        print(formatted_name, formatted_value)

    @staticmethod
    def path(path):
        """Returns a path without forbidden characters."""

        forbidden_chars = "\"*<>?|"

        path = path.replace("\\", "/")
        # Windows uses backslashes, but they are not allowed in paths

        for char in forbidden_chars:
            path = path.replace(char, "")
        return path

    @staticmethod
    def paths(*args):
        """Returns a list of paths without forbidden characters."""

        return [TextTools.path(arg) for arg in args]

    @staticmethod
    def scrap_args(cmnd):
        """Returns a list of arguments from a command."""

        quote = r'"'
        r_str = r"(?<="+ quote +r"|').*?(?="+ quote +r"|')|[^\s'"+ quote +r"]+"
        # I know this is ugly, but it works lol (regex is a pain)

        args = re_findall(r_str, cmnd)
        args = [arg.strip() for arg in args]
        args = [arg for arg in args if arg != ""]

        return args

    @staticmethod
    def color(text, color):
        """Returns a colored text."""

        formatted_color = getattr(Fore, color.upper())
        return f"{formatted_color}{text}{Style.RESET_ALL}"

    @staticmethod
    def print(text, color):
        """Prints a colored text."""

        print(TextTools.color(text, color))
