from colorama import Fore, Style
import os
import re

class TextTools:

    @staticmethod
    def indicator():
        return TextTools.color(os.getcwd()+">", "green")

    @staticmethod
    def printCommand(name, value):
        aliases = value["aliases"]
        cmnd = name
        if (len(aliases)>0): cmnd += " (" + ", ".join(aliases) + ")"
        formattedName = TextTools.color(f"{cmnd}", "yellow")
        formattedValue = f"- {value['description']}"
        print(formattedName, formattedValue)

    @staticmethod
    def path(path):
        forbidden_chars = "\"\\*<>:?|"
        for char in forbidden_chars:
            path = path.replace(char, "")
        return path
    
    @staticmethod
    def paths(*args):
        return [TextTools.path(arg) for arg in args]
    
    @staticmethod
    def scrapArgs(cmnd):
        args = re.findall("(?<=\"|').*?(?=\"|')|[^\s'\"]+", cmnd)
        args = [arg.strip() for arg in args]
        args = [arg for arg in args if arg != ""]
        return args
    
    @staticmethod
    def color(text, color):
        formattedColor = getattr(Fore, color.upper())
        return f"{formattedColor}{text}{Style.RESET_ALL}"

    @staticmethod
    def print(text, color):
        print(TextTools.color(text, color))