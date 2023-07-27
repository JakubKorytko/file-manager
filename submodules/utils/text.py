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
    def printCommand(name, value):
        """Prints a command with its description and aliases."""
        aliases = value["aliases"]
        cmnd = name
        if (len(aliases)>0): cmnd += " (" + ", ".join(aliases) + ")"
        formattedName = TextTools.color(f"{cmnd}", "yellow")
        formattedValue = f"- {value['description']}"
        print(formattedName, formattedValue)

    @staticmethod
    def path(path):
        """Returns a path without forbidden characters."""
        forbidden_chars = "\"\\*<>:?|"
        for char in forbidden_chars:
            path = path.replace(char, "")
        return path
    
    @staticmethod
    def paths(*args):
        """Returns a list of paths without forbidden characters."""
        return [TextTools.path(arg) for arg in args]
    
    @staticmethod
    def scrapArgs(cmnd):
        """Returns a list of arguments from a command."""
        args = re_findall("(?<=\"|').*?(?=\"|')|[^\s'\"]+", cmnd)
        args = [arg.strip() for arg in args]
        args = [arg for arg in args if arg != ""]
        return args
    
    @staticmethod
    def color(text, color):
        """Returns a colored text."""
        formattedColor = getattr(Fore, color.upper())
        return f"{formattedColor}{text}{Style.RESET_ALL}"

    @staticmethod
    def print(text, color):
        """Prints a colored text."""
        print(TextTools.color(text, color))