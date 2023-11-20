"""The entry point of the program."""

from os import path

from files_manager.src import FilesManager
from files_manager.src.logic import config


def set_config_path():
    """Sets the path to the config file."""

    script_dir = path.dirname(__file__)

    txt_path = "config.json"
    txt_parent_path = f"../{txt_path}"

    file = path.join(script_dir, txt_path)
    parent_file = path.join(script_dir, txt_parent_path)

    if path.isfile(parent_file):
        config.data_path = parent_file
    else:
        config.data_path = file


def main():
    """Starts the program."""
    set_config_path()
    FilesManager.start()


if __name__ == "__main__":
    main()
