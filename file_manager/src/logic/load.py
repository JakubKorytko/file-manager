"""This module is used to read the fm_config.json file and store it in a singleton class."""
from json import load as json_file_load
from sys import exit as sys_exit
from time import sleep

from file_manager.src.utils import TextTools


class Config:
    """Singleton class to load and store the fm_config.json file"""

    is_loaded = False
    _data = None
    data_path = None

    __retry_attempts = 0
    __retry_max_attempts = 3
    __retry_delay = 5

    def load_data(self):
        """Loads the fm_config.json file."""

        if self.data_path is None:
            raise ValueError("Data path is not set. Use the data_path setter.")

        try:
            with open(self.data_path, "r", encoding="utf-8") as json_file:
                self._data = json_file_load(json_file)
                self.is_loaded = True
                self.__retry_attempts = 0
        except FileNotFoundError:
            self.retry_load()

    def force_reload(self):
        """Forces the fm_config.json file to be reloaded. Useful for debugging."""

        self.is_loaded = False
        self.load_data()

    def retry_load(self):
        """Retries to load the fm_config.json file if it failed to load."""

        delay = self.__retry_delay
        attempts = self.__retry_attempts
        max_attempts = self.__retry_max_attempts

        print(f"Failed to load {self.data_path} file.")

        if attempts >= max_attempts:
            output = TextTools.color(
                f"Retried {max_attempts} times. Aborting...", "red"
            )
            print(output)
            sys_exit(1)

        time_left = delay

        while time_left > 0:
            output = f"Retrying in {time_left} seconds... (Attempt {attempts+1}/{max_attempts})"
            colored_output = TextTools.color(output, "yellow")
            print(colored_output, end="\r", flush=True)
            sleep(1)
            time_left -= 1

        print("")

        if not self.is_loaded:
            self.__retry_attempts += 1
            self.load_data()

    @property
    def data(self):
        """Getter for the fm_config.json file. Loads the file if it hasn't been loaded yet."""

        if not self.is_loaded:
            self.load_data()
        return self._data

    @data.setter
    def data(self, value):
        """Setter for the commands dictionary.
        Allows to set the commands dictionary manually. Useful for debugging."""

        self._data = value
        self.is_loaded = True


# Singleton instance
config = Config()
