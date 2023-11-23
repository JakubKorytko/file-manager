# Files Manager

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Run Super-Linter](https://github.com/JakubKorytko/files-manager/actions/workflows/super-linter.yml/badge.svg)](https://github.com/JakubKorytko/files-manager/actions/workflows/super-linter.yml)
[![Run Unit Tests](https://github.com/JakubKorytko/files-manager/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/JakubKorytko/files-manager/actions/workflows/unit_tests.yml)

## Table of Contents

- [Files Manager](#files-manager)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Prompt](#prompt)
    - [Available commands](#available-commands)
      - [Reserved commands](#reserved-commands)
  - [Extending the app](#extending-the-app)
    - [Adding new commands](#adding-new-commands)
    - [Adding new generic errors](#adding-new-generic-errors)
    - [Using error codes in the commands](#using-error-codes-in-the-commands)
      - [Command-specific errors](#command-specific-errors)
      - [Generic errors](#generic-errors)
      - [Formatting the error messages](#formatting-the-error-messages)
  - [Running tests](#running-tests)
  - [Building the app](#building-the-app)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)

## Introduction

The Files Manager is a Python console application that allows you to manage files and directories.
It works much like the `cmd` or `bash` command-line interfaces, but you can easily extend it with your own commands.

It may not seem like a very useful project on its own since you have aliases and scripts in the `cmd` and `bash` command-line interfaces,
but it can be used as a base for other projects.
For example, you can use it as the base for a file manager that has a GUI.

You can also restrict access to the commands by creating a custom interface that only allows the user to run the commands you want.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- [Python 3.11.4 or later](https://www.python.org/downloads/)
- [Poetry 1.7.1 or later](https://python-poetry.org/docs/#installation)

## Installation

1. Clone this repository to your local machine using Git,
or download the ZIP file and extract it to a directory of your choice:

    ```bash
    git clone https://github.com/JakubKorytko/files-manager.git
    ```

1. Change to the project directory:

    ```bash
    cd files-manager
    ```

1. Run the following command to install the required dependencies:

    ```bash
    poetry install
    ```

You can now run the project by executing the following command:

```bash
poetry run files-manager
```

## Usage

### Prompt

After you run the application, you will see the following prompt:

```bash
path>
```

where `path` is the current path.

You can now enter the commands and their arguments.

### Available commands

By default, the application comes with the following commands:

- `cd` - change the current path
  - Aliases: `chdir`
  - Arguments:
    - `path` - the path to the directory you want to change to

- `dir` - list the contents of the current directory
  - Aliases: `ls`
  - Arguments:
    - none

- `help` - display the help message
  - Aliases: none
  - Arguments:
    - none

- `md` - create a new directory
  - Aliases: `mkdir`
  - Arguments:
    - `path` - the path to the directory you want to create

- `rm` - remove a file or directory
  - Aliases: `del`
  - Arguments:
    - `path` - the path to the file or directory you want to remove

- `rename` - rename a file or directory
  - Aliases: `ren`
  - Arguments:
    - `path` - the path to the file or directory you want to rename
    - `new_name` - the new name of the file or directory

- `cp` - copy a file or directory
  - Aliases: `copy`
  - Arguments:
    - `path` - the path to the file or directory you want to copy
    - `destination` - the path to the destination directory

#### Reserved commands

The following commands are reserved and you cannot create a command with the same name,
although they do not have their own classes
and are not listed in the [fm_config.json](./fm_config.json) file:

- `exit` - exit the application
  - Aliases: none
  - Arguments:
    - none

- `___test_command_class` - a command used for testing purposes
  - **It can't be used in the application**

## Extending the app

### Adding new commands

To add a new command:

1. Create a new file in the [fm_commands](./fm_commands/) directory or copy [fm_commands/.example.py](./fm_commands/.example.py) and rename it.
Use the name of the command as the name of the file and follow the **snake_case** naming convention.

1. Add the following import to the file:

    ```python
    from fm_commands._base import Command
    ```

1. Create a new class that inherits from the [Command](./fm_commands/_base.py) class.
Give the class the same name as the file but in **PascalCase**:

    ```python
    class ExampleCommand(Command):
        pass
    ```

1. Add the `main` static method to the class.
You can add any other methods you need to the class,
but the `main` method is required.
There are a few rules for the `main` method:

   - The method must be static
   - This method is called when the command is executed.
   - Parameters should be:

     - `*args` - if you don't need any parameters
     - A single parameter - it will contain a list of arguments
     passed to the command

   - If you use `*args`, call the:

        ```python
        Command.no_args(args, "<command_name>")
        ```

        method at the top of the `main` method,
        where `<command_name>` is the name of the command.
        This will inform the user that the command doesn't take any arguments,
        and they will be ignored.
        It doesn't stop the execution of the command.

   - It should return a `1` if the command was executed successfully.

    Example of the `main` method that doesn't take any arguments:

    ```python
    # example_command.py
    class ExampleCommand(Command):
        @staticmethod
        def main(*args):
            Command.no_args(args, "example_command")
            return 1
    ```

    Example for the `main` method, which takes arguments
    and prints the first one to the console:

    ```python
    # example_command.py
    class ExampleCommand(Command):
        @staticmethod
        def main(params):
            print(params[0])
            return 1
    ```

1. Import the new command into [\_\_init\_\_.py](./fm_commands/__init__.py) located in the [fm_commands](./fm_commands/) directory:

    ```python
    from fm_commands.example_command import ExampleCommand
    ```

    and add it to the `__all__` list:

    ```python
    __all__ = [
        # ...
        "ExampleCommand"
    ]
    ```

1. Add the info about the new command to the [fm_config.json](./fm_config.json)
file in the project root directory.

   - Add it to the `commands` dictionary
   - Use the name of the command as the key
    **(the same as the name of the file but without the `.py` extension)**
   - Use the following properties:
     - A list of aliases for the command (key: `aliases`)
     - A description of the command (key: `description`)
     - A dictionary of error codes and their descriptions (key: `errorCodes`)
       - Use the error code as the key
       - Use the error description as the value

    Example of the [fm_config.json](./fm_config.json) file:

    ```json
    {
    "commands": {
        // ...
        "example_command": {
        "aliases": ["example", "ex"],
        "description": "Example command",
        "errorCodes": {
            "exampleError": "Example error",
            "exampleFormattedError": "Example error {example_value}"
        }
        },
        // ...
    }
    }
    ```

(For more information about the `errorCodes` property, see the [using error codes in the commands](#using-error-codes-in-the-commands) section.)

The command should now be available in the application.
You can verify that it is loaded correctly by running the following command in the application:

```bash
help
```

### Adding new generic errors

To add a new generic error,
create new key-value pair in the `genericErrorCodes` dictionary in the [fm_config.json](./fm_config.json) file:

```json
{
    // ...
    "genericErrorCodes": {
        // ...
        "exampleError": "Example error",
        "exampleFormattedError": "Example error {example_value}"
    }
}
```

### Using error codes in the commands

To use the error codes in the commands, import the [Error](./files_manager/src/utils/error.py) class:

```python
from files_manager.src.utils import Error
```

The `Error.command` and `Error.generic` methods return a string with the formatted error message.
If you want to print the error message to the console,
use the `Error.display` method:

```python
err = Error.command("example_command", "exampleFormattedError", {"example_value": "example"})
Error.display(err)
```

The [Error](./files_manager/src/utils/error.py) class is purely informational. It doesn't stop the command from executing.

#### Command-specific errors

To use the error codes defined in the specific command,
call the `Error.command` method:

```python
Error.command("<command_name>", "<error_code>")
```

where `<command_name>` is the name of the command
and `<error_code>` is the error code.

For example, if you want to use the `exampleError` error code from the `example_command` command:

```python
Error.command("example_command", "exampleError")
```

There is also a third argument that you can pass to the `Error.command` method.
It is covered in the [formatting the error messages](#formatting-the-error-messages) section.

#### Generic errors

To use the generic error codes,
call the `Error.generic` method:

```python
Error.generic("<error_code>")
```

where `<error_code>` is the error code.

For example, if you want to use the `unknownCommand` error code:

```python
Error.generic("unknownCommand")
```

There is also a second argument that you can pass to the `Error.generic` method.
It is covered in the [formatting the error messages](#formatting-the-error-messages) section.

#### Formatting the error messages

Both command-specific and generic error codes can use `{<key>}` (where `<key>` is any string) in the value to format the error message.
You can use as many keys as you like.
The third argument of the `Error.command` method and the second argument of the `Error.generic` method is a dictionary of values
that will be used to format the error message.
The keys in the dictionary must match the keys in the error message.

For example, if you want to use the `exampleFormattedError` error code from the `example_command` command
and pass the value of `example_value` to the error message when the error message contains `{example_value}`:

```python
Error.command("example_command", "exampleFormattedError", {"example_value": "example"})
```

And the same goes for the generic errors:

```python
Error.generic("exampleFormattedError", {"example_value": "example"})
```

**Important:** If you want to use the `{<key>}` (where `<key>` is any string) placeholder(s) in the error message,
you must pass the dictionary as the second argument
to the `Error.command` or `Error.generic` method every time you call it.
The application will throw an error if you don't pass the dictionary of values
and the error message contains the placeholder(s).

## Running tests

To run the tests, run the following command:

```bash
poetry run pytest
```

## Building the app

To build the application, run the following command:

```bash
poetry build
```

The built application will be located in the `dist` directory.
It should contain `.whl` and `.tar.gz` files. You can install the application by running the following command:

```bash
pip install <path-to-whl-or-tar.gz-file>
```

## Contributing

If you find issues or have suggestions for improvements,
feel free to open an issue or submit a pull request.
Contributions are welcome!

## Contact

If you have any questions, feel free to contact me at <jakub@korytko.me>.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
