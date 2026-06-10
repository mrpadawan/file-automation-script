# M122 File Organizer

## Overview

M122 File Organizer is a Python automation project for organizing downloaded school files. The application scans a configured input folder, extracts module identifiers from filenames such as `M122` or `M114`, and moves files into the correct module folders.

The project demonstrates practical process automation with a modular Python architecture, configuration management, logging, duplicate handling, a Tkinter GUI, Discord webhook reporting, and Windows Task Scheduler integration.

## Features

* Automatic file detection from a configured input folder
* Module identifier extraction from filenames
* Configurable module-to-folder mapping
* Extension-based subfolder categorization
* Automatic creation of missing destination folders
* Duplicate filename handling with `_V2`, `_V3`, and later suffixes
* Tkinter graphical user interface
* File selection with checkboxes
* Select All and Deselect All controls
* Scrollable file list
* Progress bar and status messages
* Structured logging
* Discord webhook reports
* Manual, daily, and weekly reporting support
* Windows Task Scheduler integration
* Executable build support with PyInstaller
* Unit test structure and professional testing documentation

## Technologies

* Python 3
* Tkinter
* pathlib and shutil
* Python logging
* Environment variables
* JSON configuration
* python-dotenv
* discord-webhook
* Windows Task Scheduler
* unittest
* PyInstaller

## Project Structure

```txt
project-root/
├── assets/
│   └── icon.ico
├── config/
│   └── module_mapping.json
├── docs/
│   ├── design/
│   │   ├── architecture/
│   │   └── diagrams/
│   ├── grading/
│   ├── requirements/
│   └── testing/
│       ├── debugging.md
│       ├── test_cases.md
│       └── test_protocol.md
├── src/
│   ├── config.py
│   ├── detector.py
│   ├── discord_reporter.py
│   ├── gui.py
│   ├── gui_discord.py
│   ├── gui_file_operations.py
│   ├── gui_helpers.py
│   ├── gui_selection.py
│   ├── gui_state.py
│   ├── logger.py
│   ├── main.py
│   ├── mover.py
│   ├── parser.py
│   ├── scheduler_runner.py
│   └── weekly_report_runner.py
├── tests/
│   ├── test_files/
│   │   ├── duplicates/
│   │   ├── empty/
│   │   ├── invalid/
│   │   └── valid/
│   ├── test_detector.py
│   ├── test_discord.py
│   ├── test_gui.py
│   ├── test_mover.py
│   └── test_parser.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Configuration

The application uses environment variables and a JSON mapping file.

Example `.env` configuration:

```env
DOWNLOADS_PATH=./input
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=./output/unknown
MAPPING_FILE=./config/module_mapping.json
MANUAL_DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
DAILY_DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
WEEKLY_DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

Example `config/module_mapping.json`:

```json
{
    "modules": {
        "M122": "./output/M122",
        "M123": "./output/M123",
        "M114": "./output/M114"
    },
    "subfolders": {
        "exercise": "Exercises",
        "theory": "Theory",
        "code": "Code"
    }
}
```

## Installation

Clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd file-automation-script
pip install -r requirements.txt
```

Create a local `.env` file from `.env.example` and adjust the paths and webhook URLs for your environment.

## Usage

Run the main automation:

```bash
python src/main.py
```

Run the graphical interface:

```bash
python src/gui.py
```

The GUI supports file scanning, checkbox-based file selection, Select All and Deselect All actions, progress updates, status messages, and a processing summary.

## Discord Reporting

Discord webhook reporting is handled through `src/discord_reporter.py` and the configured webhook URLs.

Supported report types:

* Manual reports
* Daily reports
* Weekly reports

## Scheduled Automation

The project supports automated execution through Windows Task Scheduler.

Typical scheduled workflows:

* Daily file organization and reporting
* Weekly file organization and reporting

The scheduler runner scans the configured input folder, organizes files, records processing information, and can send Discord reports based on the configured workflow.

## Testing

The project includes a professional testing structure based on Python `unittest`.

Run all tests:

```bash
.venv\Scripts\python.exe -m unittest discover tests
```

Testing assets and documentation are organized as follows:

```txt
tests/
├── test_files/
│   ├── valid/
│   ├── invalid/
│   ├── duplicates/
│   └── empty/
│   ├── debugging.md
│   ├── test_cases.md
│   ├── test_protocol.md
├── test_detector.py
├── test_parser.py
├── test_mover.py
├── test_gui.py
└── test_discord.py

docs/testing/
├── debugging.md
├── test_cases.md
└── test_protocol.md
```

## Build Executable

Build the GUI as a Windows executable:

```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico --name="M122 File Organizer" src/gui.py
```

The executable is created in the `dist/` folder.

## Documentation

Project documentation includes:

* Requirements documentation
* Architecture documentation
* UML diagrams
* File detection workflow
* Parsing logic
* Logging architecture
* Error handling strategy
* Test cases
* Test protocol

## Author

Nikola

GIBZ Informatik  
Module 122 - Automating Processes with a Scripting Language
