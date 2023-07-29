""" This file is used to import all the classes in the commands folder."""

from ._base import Command
from .dir import Dir
from .help import Help
from .cd import Cd
from .md import Md
from .rm import Rm
from .rename import Rename
from .cp import Cp

# To add a new command import, do it like that:
# from .<command_name> import <Command_name>
