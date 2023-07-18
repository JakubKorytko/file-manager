from submodules.utils import TextTools, data

class Error:

    commands = data["commands"]
    genericCodes = data["genericErrorCodes"]

    @staticmethod
    def generic(code, args={}):
        return Error.genericCodes[code].format(**args)

    @staticmethod
    def command(command, code, args={}):
        return Error.commands[command]["errorCodes"][code].format(**args)
    
    @staticmethod
    def display(error):
        TextTools.print(error, "red")