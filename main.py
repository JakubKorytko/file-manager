"""The entry point of the program."""
# from filesmanager import FilesManager

# FilesManager.start()

from commands import CommandsHandler

CommandsHandler.run("ls", [])