""" This file is used to import all the classes in the commands folder."""

from files_manager.commands._base import Command
from files_manager.commands.cd import Cd
from files_manager.commands.cp import Cp
from files_manager.commands.dir import Dir
from files_manager.commands.help import Help
from files_manager.commands.md import Md
from files_manager.commands.rename import Rename
from files_manager.commands.rm import Rm

# To add a new command import, do it like that:
# from commands.<command_name> import <Command_name>

# Then add it to the __all__ list:
__all__ = ["Command", "Cd", "Cp", "Dir", "Help", "Md", "Rename", "Rm"]
