from colorama import init as colorama_init
from submodules import TextTools, Error
from commands import Commands

class FileManager:

    @staticmethod
    def start():
        FileManager.init()
        FileManager.loop()

    @staticmethod
    def init():
        colorama_init()
        TextTools.print('\nFile manager (use "exit" to exit, "help" to list commands)\n', "magenta")

    @staticmethod
    def run(cmnd):
    
        args = TextTools.scrapArgs(cmnd)

        if (len(args) == 0): return 1
        command = args[0]

        command_f = Commands.run(command)

        if (command_f == False):
            error = Error.generic("unknownCommand", {"command": command})
            Error.display(error)
            return 1

        command_f(args[1:])
        return 1

    @staticmethod
    def loop():
        while FileManager.run(input(TextTools.indicator())): pass