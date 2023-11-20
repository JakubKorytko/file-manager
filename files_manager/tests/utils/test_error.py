"""Tests for the Error module"""

from json import load as json_load
from os import path

from colorama import Fore, Style

from files_manager.src.utils import Error


class TestError:
    """Class containing all the tests for the Error module"""

    test_data_path = path.join(path.dirname(__file__), "test_data.json")

    with open(test_data_path, "r", encoding="utf-8") as file:
        test_data = json_load(file)

    @staticmethod
    def test_set_data():
        """Tests the Error.set_data() method"""

        Error.set_data(TestError.test_data)

        assert Error.commands == TestError.test_data["commands"]
        assert Error.generic_codes == TestError.test_data["genericErrorCodes"]
        assert Error.data_loaded

        Error.unset_data()

    @staticmethod
    def test_error_display(capfd):
        """Tests the Error.display() method"""

        test_text = "Test"
        error_color = "red"

        Error.display("Test")

        formatted_color = getattr(Fore, error_color.upper())
        colored_text = f"{formatted_color}{test_text}{Style.RESET_ALL}"

        out, _ = capfd.readouterr()
        assert out == f"{colored_text}\n"

    @staticmethod
    def test_call_without_set_data():
        """Tests calling methods that require Error.set_data() without calling it"""

        expected_message_command = Error.not_loaded_message("command")
        expected_message_generic = Error.not_loaded_message("generic")

        got_message_command = Error.command("test", "test")
        got_message_generic = Error.generic("test")

        assert expected_message_command == got_message_command
        assert expected_message_generic == got_message_generic

    @staticmethod
    def test_call_with_set_data():
        """Tests calling methods that require Error.set_data() after calling it"""

        Error.set_data(TestError.test_data)

        expected_message_command = "The path is not a directory"
        expected_message_generic = (
            "Unknown command: test, type 'help' to see available commands"
        )

        got_message_command = Error.command("cd", "notDirectory")
        got_message_generic = Error.generic("unknownCommand", {"command": "test"})

        assert expected_message_command == got_message_command
        assert expected_message_generic == got_message_generic

        Error.unset_data()
