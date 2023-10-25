""" This file is used to import all the classes in the commands folder."""

from commands._base import Command
from commands.dir import Dir
from commands.help import Help
from commands.cd import Cd
from commands.md import Md
from commands.rm import Rm
from commands.rename import Rename
from commands.cp import Cp

# To add a new command import, do it like that:
# from commands.<command_name> import <Command_name>
