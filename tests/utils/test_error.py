"""Tests for the Error module"""

from colorama import Fore, Style
from utils import Error

class TestError:
    """Class containing all the tests for the Error module"""

    data = {
        "commands": {
            "cd": {
                "aliases": [
                    "chdir"
                ],
                "description": "changes to the selected directory",
                "errorCodes": {
                    "notDirectory": "The path is not a directory",
                    "notFound": "The path does not exist"
                }
            },
            "md": {
                "aliases": [
                    "mkdir"
                ],
                "description": "creates a directory with the given name",
                "errorCodes": {
                    "alreadyExists": "The directory already exists"
                }
            }
            },
        "genericErrorCodes": {
            "unknownCommand": "Unknown command: {command}, type 'help' to see available commands",
            "invalidSyntax": "Invalid command syntax"
        }
    }

    @staticmethod
    def test_set_data():
        """Tests the Error.set_data() method"""

        Error.set_data(TestError.data)

        assert Error.commands == TestError.data["commands"]
        assert Error.generic_codes == TestError.data["genericErrorCodes"]
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

        Error.set_data(TestError.data)

        expected_message_command = "The path is not a directory"
        expected_message_generic = "Unknown command: test, type 'help' to see available commands"

        got_message_command = Error.command("cd", "notDirectory")
        got_message_generic = Error.generic("unknownCommand", {"command": "test"})

        assert expected_message_command == got_message_command
        assert expected_message_generic == got_message_generic

        Error.unset_data()
