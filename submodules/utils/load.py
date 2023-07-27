"""This module is used to read the config.json file and store it in a singleton class."""
import os
import json

class Config:
    """Singleton class to load and store the config.json file"""

    is_loaded = False
    _data = None

    def load_data(self):
        """Loads the config.json file."""
        script_dir = os.path.dirname(__file__)
        txt_path = "config.json"
        file = os.path.join(script_dir, txt_path)

        with open(file, "r", encoding="utf-8") as jsonFile:
            self._data = json.load(jsonFile)
            self.is_loaded = True

    def force_reload(self):
        """Forces the config.json file to be reloaded. Useful for debugging."""
        self.is_loaded = False
        self.load_data()

    @property
    def data(self):
        """Getter for the config.json file. Loads the file if it hasn't been loaded yet."""
        if not self.is_loaded:
            self.load_data()
        return self._data

# Singleton instance
Config = Config()
