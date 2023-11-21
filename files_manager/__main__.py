"""The entry point of the program."""

from os import path

from files_manager.src import FilesManager


def main():
    """Starts the program."""
    script_dir = path.dirname(path.realpath(__file__))
    FilesManager.start(script_dir)


if __name__ == "__main__":
    main()
