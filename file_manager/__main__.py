"""The entry point of the program."""

from os import path

from file_manager.src import FileManager


def main():
    """Starts the program."""
    script_dir = path.dirname(path.realpath(__file__))
    FileManager.start(script_dir)


if __name__ == "__main__":
    main()
