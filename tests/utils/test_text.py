"""Unit tests for the TextTools module."""

from os import getcwd
from colorama import Fore, Style
from utils import TextTools

class TestTextTools:
    """Class containing all the tests for the TextTools module"""

    test_command_name = "cd"
    test_command = {
        "aliases": [
            "chdir"
        ],
        "description": "changes to the selected directory",
        "errorCodes": {
            "notDirectory": "The path is not a directory",
            "notFound": "The path does not exist"
        }
    }

    @staticmethod
    def test_indictor():
        """Tests the indicator() method"""

        indicator_string = f"{getcwd()}>"
        indicator_color = "green"

        formatted_color = getattr(Fore, indicator_color.upper())
        formatted_text = f"{formatted_color}{indicator_string}{Style.RESET_ALL}"

        res = TextTools.indicator()

        assert res == formatted_text

    @staticmethod
    def test_print_command(capfd):
        """Tests the TextTools.print_command() method"""

        command_name = TestTextTools.test_command_name
        command_description = TestTextTools.test_command["description"]
        command_aliases = TestTextTools.test_command["aliases"]

        aliases = " (" + ", ".join(command_aliases) + ")"

        cmnd = f"{command_name}{aliases}"

        formatted_color = getattr(Fore, "yellow".upper())
        formatted_cmnd = f"{formatted_color}{cmnd}{Style.RESET_ALL}"

        formatted_description = f"- {command_description}"

        TextTools.print_command(command_name, TestTextTools.test_command)

        out, _ = capfd.readouterr()

        assert out == formatted_cmnd + " " + formatted_description + "\n"

    @staticmethod
    def test_path():
        """Tests the TextTools.path() method"""

        test_path = "C:\\Users\\User\\Documents\\test.txt*?<>"
        result_path = "C:/Users/User/Documents/test.txt"
        # Windows uses backslashes, but they are not allowed in paths
        # They are replaced by slashes
        # Also, the forbidden characters are removed

        res = TextTools.path(test_path)

        assert res == result_path

    @staticmethod
    def test_paths():
        """Tests the TextTools.paths() method"""

        test_paths = [
            "C:\\Users\\User\\Documents\\test.txt*?<>",
            "*?C:\\Users\\User\\Desktop\\test.txt<>"
        ]
        result_paths = [
            "C:/Users/User/Documents/test.txt",
            "C:/Users/User/Desktop/test.txt"
        ]
        # Windows uses backslashes, but they are not allowed in paths
        # They are replaced by slashes
        # Also, the forbidden characters are removed

        res = TextTools.paths(*test_paths)

        assert res == result_paths


    @staticmethod
    def test_scrap_args():
        """Tests the TextTools.scrap_args() method"""

        test_command = 'cp   \'/home/user/Documents\'    "/home/user/Desktop"   '
        # Spaces are here to test the strip() method
        # Quotes are here to test the regex

        test_args = ["cp", "/home/user/Documents", "/home/user/Desktop"]

        res = TextTools.scrap_args(test_command)

        assert res == test_args

    @staticmethod
    def test_color():
        """Tests the TextTools.color() method"""

        test_colors = ["red", "green", "yellow"]
        test_texts = ["Test1", "Test2", "Test3"]

        if len(test_colors) != len(test_texts):
            raise ValueError("The number of colors and texts must be the same")

        iterations = len(test_colors)

        for i in range(iterations):
            formatted_color = getattr(Fore, test_colors[i].upper())
            formatted_text = f"{formatted_color}{test_texts[i]}{Style.RESET_ALL}"

            res = TextTools.color(test_texts[i], test_colors[i])
            assert res == formatted_text

    @staticmethod
    def test_print(capfd):
        """Tests the TextTools.print() method"""

        test_colors = ["red", "green", "yellow"]
        test_texts = ["Test1", "Test2", "Test3"]

        if len(test_colors) != len(test_texts):
            raise ValueError("The number of colors and texts must be the same")

        iterations = len(test_colors)

        for i in range(iterations):
            formatted_color = getattr(Fore, test_colors[i].upper())
            formatted_text = f"{formatted_color}{test_texts[i]}{Style.RESET_ALL}"

            TextTools.print(test_texts[i], test_colors[i])
            out, _ = capfd.readouterr()
            assert out == formatted_text + "\n"
