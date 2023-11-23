""" Tests for logic.handler module. """

# In order to test the protected methods, we need to call them
# but there is no need to call it in the actual code
# so we can disable the protected access warning

# pylint: disable=protected-access

# ___TestCommandClass name is used to avoid name conflicts
# with the actual command classes, so we can disable invalid name warning

# pylint: disable=invalid-name

from pytest import raises

from files_manager.src.logic import CommandsHandler
from fm_commands import Command


class TestCommandsHandler:
    """Tests for CommandsHandler class."""

    @staticmethod
    def test_set_data():
        """Test for CommandsHandler.set_data() method."""

        data = {"commands": ["test"]}

        CommandsHandler.set_data(data, Command.__subclasses__())
        assert CommandsHandler.data == data

    @staticmethod
    def test_wrong_data_message(capsys):
        """Test for CommandsHandler.wrong_data_message() method."""

        with raises(SystemExit):
            CommandsHandler.wrong_data_message()
            captured = capsys.readouterr()
            assert "Fix it by adding/removing a command class" in captured.out

    @staticmethod
    def test_verify(monkeypatch, capsys):
        """Test for CommandsHandler._verify() method."""

        data = {"commands": ["___testcommandclass"]}

        # We need to check if the class is in the list of subclasses
        # we don't use any of the methods,
        # so we can disable too-few-public-methods warning

        # pylint: disable=too-few-public-methods

        class ___TestCommandClass(Command):
            """Test class to insert into Command.__subclasses__()."""

        def mock_subclasses():
            return [___TestCommandClass]

        monkeypatch.setattr(Command, "__subclasses__", mock_subclasses)

        CommandsHandler.set_data(data, Command.__subclasses__())

        CommandsHandler._verify()

        captured = capsys.readouterr()

        assert (
            "Number of commands does not match the number of command classes"
            not in captured.out
        )

    @staticmethod
    def test_convert_if_alias():
        """Test for CommandsHandler._convert_if_alias() method."""

        data = {"commands": {"test": {"aliases": ["alias"]}}}
        CommandsHandler.set_data(data, Command.__subclasses__())

        assert CommandsHandler._convert_if_alias("test") == "test"
        assert CommandsHandler._convert_if_alias("alias") == "test"
        assert CommandsHandler._convert_if_alias("unknown") == "unknown"

    @staticmethod
    def test_run(monkeypatch):
        """Test for CommandsHandler.run() method."""

        data = {"commands": ["___testcommandclass"]}

        class ___TestCommandClass(Command):
            """Test class to insert into Command.__subclasses__()."""

            @staticmethod
            def main():
                """Empty main method."""
                return True

        def mock_subclasses():
            return [___TestCommandClass]

        def mock_convert_if_alias(command):
            return command

        monkeypatch.setattr(Command, "__subclasses__", mock_subclasses)
        monkeypatch.setattr(CommandsHandler, "_convert_if_alias", mock_convert_if_alias)

        CommandsHandler.set_data(data, Command.__subclasses__())

        returned_main_method = CommandsHandler.run("___testcommandclass")

        # We need to compare the actual method, not the result of calling it
        # so we can disable comparison-with-callable warning

        # pylint: disable=comparison-with-callable

        assert returned_main_method == ___TestCommandClass.main
        assert CommandsHandler.run("unknown") is False

    @staticmethod
    def test_run_exit():
        """Test for CommandsHandler.run() method."""

        with raises(SystemExit):
            CommandsHandler.run("exit")([])
