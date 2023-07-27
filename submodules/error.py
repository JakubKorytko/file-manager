from submodules.utils import TextTools, Config

class Error:

    commands = Config.data["commands"]
    genericCodes = Config.data["genericErrorCodes"]

    @staticmethod
    def generic(code, args={}):
        return Error.genericCodes[code].format(**args)

    @staticmethod
    def command(command, code, args={}):
        return Error.commands[command]["errorCodes"][code].format(**args)
    
    @staticmethod
    def display(error):
        TextTools.print(error, "red")