""" This file is used to import all the classes in the commands folder."""

from fm_commands._base import Command
from fm_commands.cd import Cd
from fm_commands.cp import Cp
from fm_commands.dir import Dir
from fm_commands.help import Help
from fm_commands.md import Md
from fm_commands.rename import Rename
from fm_commands.rm import Rm

# To add a new command, import it here:
# from fm_commands.<command_name> import <Command_name>

# Then add it to the __all__ list:
__all__ = ["Command", "Cd", "Cp", "Dir", "Help", "Md", "Rename", "Rm"]
