# Files manager

- [Files manager](#files-manager)
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Features](#features)
- [Configuration](#configuration)
    - [Adding new commands](#adding-new-commands)
- [License](#license)


# Introduction

files-manager is a console application written in Python that provides basic files managing functions. It allows users to view files and folders, change directories, create new directories, delete files and directories, rename files and directories, and copy files and directories.

This project was created to provide a simple, yet powerful tool for managing files and directories in a console environment. It can be used by developers, system administrators, or anyone who needs to work with files and directories on a daily basis.

With its intuitive and easy-to-use interface, files-manager is a great tool for managing files and directories quickly and efficiently.

# Prerequisites

Before you can use files-manager, you must have the following installed on your machine:

Python 3.6 or higher
You can check if you have Python installed by running the following command in your terminal:

```bash
python --version
```

If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

# Installation

To install files-manager, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/JakubKorytko/files-manager.git
```

2. Change to the project directory:

```bash
cd files-manager
```
3. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

That's it! Now you're ready to run files-manager on your machine.

# How to Run
To run files-manager, follow these steps:

Open a terminal or command prompt.

1. Change to the project directory:

```bash
cd files-manager
```
2. Run the following command:

```bash
python main.py
```
That's it! Now you can use files-manager to manage files and directories from the console.

# Features
files-manager provides the following features:

- **dir (ls)**: displays files and folders in the current directory.
- **help**: displays available commands.
- **cd (chdir)**: changes to the selected directory.
- **md (mkdir)**: creates a directory with the given name.
- **rm (del)**: deletes the file/directory at the given path.
- **rename (ren)**: renames a file/directory.
- **cp (copy)**: copies a file/directory from the source path to the destination path.

You can also use aliases in the brackets for some of these commands. For example, **ls** is an alias for the **dir** command, and **chdir** is an alias for the **cd** command. These aliases are provided for convenience and to make the tool easier to use for users who are familiar with other command-line interfaces.

# Configuration

files-manager comes with a configuration file called **config.json**. This file is located in the **/submodules/utils/config.json** path.

The config.json file allows you to customize files-manager by adding new commands, changing existing commands, or modifying error messages.

The file consists of two sections:

- commands: This section contains a list of commands that files-manager understands. The command includes aliases for the command, a description of what the command does, and error codes that are used if the command fails.

- genericErrorCodes: This section contains a list of error codes that are used by files-manager when a command fails. These errors are used by multiple commands, so they are stored in a separate section to avoid duplication.

Here's an initial config.json file:

```json
{
    "commands": {
        "dir": {
            "aliases": [
                "ls"
            ],
            "description": "displays files and folders in the current directory"
        },
        "help": {
            "aliases": [],
            "description": "displays available commands"
        },
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
        },
        "rm": {
            "aliases": [
                "del"
            ],
            "description": "deletes the file/directory at the given path",
            "errorCodes": {
                "notFound": "The path does not exist"
            }
        },
        "rename": {
            "aliases": [
                "ren"
            ],
            "description": "renames a file/directory",
            "errorCodes": {
                "alreadyExists": "The destination directory name already exists",
                "notFound": "The path of the file/directory you want to rename does not exist"
            }
        },
        "cp": {
            "aliases": [
                "copy"
            ],
            "description": "copies a file/directory from the source path to the destination path",
            "errorCodes": {
                "alreadyExists": "Directory/file with the new name already exists",
                "notFound": "The path of the file/directory to be copied does not exist"
            }
        }
    },
    "genericErrorCodes": {
        "unknownCommand": "Unknown command: {command}, type 'help' to see available commands",
        "invalidSyntax": "Invalid command syntax",
        "unknownError": "Unknown error occured",
        "invalidArguments": "Invalid arguments, expected {expected}, got {actual}"
    }
}
```

### Adding new commands

You can customize this file to better suit your needs. If you add a new command, you must also add a new static method to the **Commands** class in the **/submodules/utils/command.py** file. This method must have the same name as the command you added to the config.json file.

# License

files-manager is licensed under the MIT License, which means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. But you must include the original license in all copies or substantial portions of the software.

However, I do appreciate attribution if you use my work!