""" This file is used to import all the classes in the commands folder."""

from commands._base import Command
from commands.cd import Cd
from commands.cp import Cp
from commands.dir import Dir
from commands.help import Help
from commands.md import Md
from commands.rename import Rename
from commands.rm import Rm

# To add a new command, import it here:
# from commands.<command_name> import <Command_name>

# Then add it to the __all__ list:
__all__ = ["Command", "Cd", "Cp", "Dir", "Help", "Md", "Rename", "Rm"]
