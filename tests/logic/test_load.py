""" Test the load module. """

from unittest.mock import patch, mock_open
from pytest import raises

from logic.load import Config


class TestConfig:
    """Test the Config class."""

    @staticmethod
    def test_load_data():
        """Test the load_data() method."""

        config = Config()
        with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
            config.load_data()
        assert config.is_loaded is True
        assert config.data == {"key": "value"}

    @staticmethod
    def test_force_reload():
        """Test the force_reload() method."""

        config = Config()
        with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
            config.load_data()
        assert config.is_loaded is True
        assert config.data == {"key": "value"}

        with patch("builtins.open", mock_open(read_data='{"key": "new_value"}')):
            config.force_reload()
        assert config.is_loaded is True
        assert config.data == {"key": "new_value"}

    @staticmethod
    def test_retry_load(monkeypatch):
        """Test the retry_load() method."""

        monkeypatch.setattr(Config, "_Config__retry_delay", 0)
        monkeypatch.setattr(Config, "_Config__retry_max_attempts", 1)

        config = Config()

        with patch("builtins.open", side_effect=FileNotFoundError):
            with raises(SystemExit):
                config.load_data()

        with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
            config.load_data()

        assert config.is_loaded is True
        assert config.data == {"key": "value"}

    @staticmethod
    def test_data_setter():
        """Test the data setter."""

        config = Config()
        config.data = {"key": "value"}
        assert config.is_loaded is True
        assert config.data == {"key": "value"}
