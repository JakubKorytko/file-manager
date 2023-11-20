"""Package for the logic of the program."""

from files_manager.src.logic import CommandsHandler, Config
from files_manager.src.main import FilesManager
from files_manager.src.utils import Error, TextTools

__all__ = ["Error", "TextTools", "CommandsHandler", "FilesManager", "Config"]
