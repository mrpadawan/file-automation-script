# M122 File Organizer

A configurable Python application that organizes downloaded school files into
the correct module and file-type folders.

> New user? Start with [INSTRUCTIONS.md](INSTRUCTIONS.md) for the complete
> installation guide after downloading or extracting the ZIP file.

## Documentation Guide

- [Introduction and Context](#1-introduction-and-context)
- [Main Features](#2-main-features)
- [How the Application Works](#3-how-the-application-works)
- [Requirements](#4-requirements)
- [Quick Start](#5-quick-start)
- [Configuration](#6-configuration)
- [Running the Project](#7-running-the-project)
- [Testing and Verification](#9-testing-and-verification)
- [Troubleshooting](#10-troubleshooting)
- [Architecture and Design](#12-architecture-and-design)
- [Development Process](#13-development-process)

## 1. Introduction and Context

School files downloaded from Microsoft Teams, GitLab, browsers, and other
platforms normally arrive in one Downloads folder. Assignments, theory
documents, source code, archives, and installers then have to be moved manually
into folders such as `M122`, `M114`, or `M293`. Repeating this task every day
takes time and can lead to misplaced files, forgotten documents, and accidental
overwrites.

The M122 File Organizer automates that local workflow. It scans a configured
folder, finds a module identifier such as `M122` in each file or folder name,
resolves the configured destination, selects a category for files based on the
file extension, and moves the item safely.

The project began as the **Automated Download Organizer for School** described
in the project proposal. The original goal was a command-line script for file
detection, module parsing, folder mapping, file movement, duplicate handling,
and logging. During development, the scope was extended with a Tkinter GUI,
selective processing, progress feedback, Discord reports, scheduled runners,
and automated tests.

### Purpose

The application is intended to:

- reduce repetitive manual sorting;
- keep school module folders consistent;
- prevent existing files from being overwritten;
- make paths and module mappings configurable;
- provide a traceable workflow through logs and reports;
- remain easy to extend when new modules or file types are added.

### Scope

The current version supports local Windows file organization. A user can run it
through the GUI, from the command line, or with Windows Task Scheduler.

The application does **not** continuously watch the folder in real time. Each
manual or scheduled execution performs one scan and processes the files that
are present at that moment. It also does not provide cloud synchronization or
multi-user access.

## 2. Main Features

- Version 1.1.0.
- Scans a configurable input folder for files and direct child folders.
- Detects module codes using the name pattern `M<number>` or `M<number>E`.
- Maps known modules to destinations in `config/module_mapping.json`.
- Routes unknown or missing module codes to a configurable fallback folder.
- Sorts files into `Exercises`, `Theory`, `Code`, `Archives`, or `Executables`.
- Moves folders as complete units into the module root folder.
- Creates missing destination and category folders automatically.
- Protects existing files with `_V2`, `_V3`, and later version suffixes.
- Provides a Tkinter GUI with checkboxes and file selection controls.
- Shows detected/selected counts, progress, status, and processed files.
- Writes application events to `logs/application.log`.
- Supports optional manual, daily, and weekly Discord webhook reports.
- Includes entry points for Windows Task Scheduler.
- Includes 20 automated unit tests.

## 3. How the Application Works

The implementation follows the activity and component diagrams in
`docs/design/diagrams`.

1. The application loads `.env`.
2. `src/config.py` validates the required paths and loads the JSON mapping.
3. `src/detector.py` scans the configured input folder.
4. `src/parser.py` searches each item name for an `M<number>` identifier.
5. `src/mover.py` resolves the module or fallback destination.
6. Files use their extension to determine a category subfolder.
7. Missing folders are created.
8. Duplicate names receive the next available version suffix.
9. The file or folder is moved and the result is shown or logged.
10. When configured, a Discord summary is sent.

### Example

Given this file:

```text
M122_ProjectDocumentation.pdf
```

and this module mapping:

```json
"M122": "./output/M122"
```

the result is:

```text
./output/M122/Theory/M122_ProjectDocumentation.pdf
```

If that filename already exists, the new file becomes:

```text
M122_ProjectDocumentation_V2.pdf
```

Folders are moved as complete units. For example, `M122E_ProjectFolder` is moved
directly into the configured `M122` module destination, and its contents stay
inside the folder.

## 4. Requirements

### Supported Environment

- Windows 10 or Windows 11
- Python 3.10 or newer
- `pip`
- Tkinter, normally included with the standard Windows Python installer
- Internet access only for dependency installation and optional Discord reports

The project was most recently verified with Python `3.14.4`.

### Python Dependencies

All third-party dependencies and their pinned versions are listed in
`requirements.txt`. The main runtime packages are:

- `python-dotenv` for `.env` configuration;
- `discord-webhook` and `requests` for optional Discord reports;
- `pyinstaller` and related packages for executable builds.

Python standard-library modules such as `tkinter`, `pathlib`, `shutil`,
`logging`, `json`, `re`, and `unittest` are also used.

## 5. Quick Start

The full beginner-friendly procedure is in [INSTRUCTIONS.md](INSTRUCTIONS.md).
The short version is:

```powershell
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
New-Item -ItemType Directory -Path .\input -Force
python .\src\gui.py
```

Before launching, edit `.env` and `config/module_mapping.json` as explained
below. The included mapping contains example paths from the developer's school
computer and must be adapted on another computer.

## 6. Configuration

Configuration is intentionally kept outside the source code. This makes the
same application usable with different Windows accounts and folder structures.

### `.env`

Create `.env` by copying `.env.example`:

```powershell
Copy-Item .env.example .env
```

Example for testing entirely inside the project folder:

```env
DOWNLOADS_PATH=./input
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=./output/unknown
MAPPING_FILE=./config/module_mapping.json

MANUAL_DISCORD_WEBHOOK_URL=
DAILY_DISCORD_WEBHOOK_URL=
WEEKLY_DISCORD_WEBHOOK_URL=
```

Example using the real Windows Downloads folder:

```env
DOWNLOADS_PATH=C:/Users/YourName/Downloads
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=C:/Users/YourName/Documents/School/Unknown
MAPPING_FILE=./config/module_mapping.json
```

Use forward slashes in Windows paths. Do not add quotation marks unless the
path value itself requires them.

| Variable | Required | Purpose |
|---|---:|---|
| `DOWNLOADS_PATH` | Yes | Folder scanned for files. It must already exist. |
| `LOG_PATH` | Yes | Folder in which `application.log` is created. |
| `DEFAULT_UNKNOWN_PATH` | Yes | Destination for unconfigured or missing module codes. |
| `MAPPING_FILE` | Yes | Location of the module mapping JSON file. |
| `MANUAL_DISCORD_WEBHOOK_URL` | No | Report sent after a GUI sorting run. |
| `DAILY_DISCORD_WEBHOOK_URL` | No | Report sent by the daily scheduled runner. |
| `WEEKLY_DISCORD_WEBHOOK_URL` | No | Report sent by the weekly report runner. |

The `.env` file may contain private webhook URLs and is excluded by
`.gitignore`. Do not publish real webhook URLs.

### `config/module_mapping.json`

This file connects module codes to destination folders and category keys to
folder names:

```json
{
    "modules": {
        "M122": "C:/Users/YourName/Documents/School/M122",
        "M114": "C:/Users/YourName/Documents/School/M114"
    },
    "subfolders": {
        "exercise": "Exercises",
        "executables": "Executables",
        "archives": "Archives",
        "theory": "Theory",
        "code": "Code"
    }
}
```

Important rules:

- Keep the JSON braces, commas, and quotation marks valid.
- Add one entry for each module that should have its own destination.
- Use forward slashes in Windows paths.
- Destination folders do not need to exist; the program creates them.
- A module absent from this file uses `DEFAULT_UNKNOWN_PATH`.

### Name Convention

The parser searches for an uppercase `M` followed by digits anywhere in the
file or folder name. A trailing `E` suffix is also accepted:

```text
M122_Project.pdf
LB02_M114_Exercise.docx
Notes_M293.txt
M122E_ProjectFolder
```

These names produce `M122`, `M114`, `M293`, and `M122E`. A name such as
`Homework.pdf` has no module match and is sent to the fallback destination.
Lowercase `m122` is not recognized by the current parser.

### File Categories

| Category folder | Common extensions |
|---|---|
| `Exercises` | `.docx`, `.xlsx`, `.pptx`, `.odt`, `.rtf` |
| `Theory` | `.pdf`, `.md`, `.txt`, `.epub` |
| `Code` | `.py`, `.java`, `.js`, `.html`, `.css`, `.sql`, `.json`, `.xml` |
| `Archives` | `.zip`, `.7z`, `.rar`, `.tar`, `.gz`, `.iso` |
| `Executables` | `.exe`, `.bat`, `.cmd`, `.msi`, `.ps1`, `.jar` |

An extension without a defined category is moved directly into the module's
base destination.

## 7. Running the Project

Run commands from the project root, where `README.md` and `requirements.txt`
are located.

### Graphical Interface

```powershell
.\.venv\Scripts\python.exe .\src\gui.py
```

GUI workflow:

1. Click **Scan Files**.
2. Review the detected files.
3. Use the checkboxes, **Select All**, or **Deselect All**.
4. Click **Execute Sorting**.
5. Review the progress bar, status, and processed-file list.
6. Check the configured destinations and `logs/application.log`.

Files are moved, not copied. Test with `DOWNLOADS_PATH=./input` before pointing
the application at a real Downloads folder.

### Command-Line Workflow

```powershell
.\.venv\Scripts\python.exe .\src\main.py
```

This scans once and processes every file in the configured input folder.

### Daily Scheduled Workflow

```powershell
.\.venv\Scripts\python.exe .\src\scheduler_runner.py
```

This processes all detected files and attempts to send a daily Discord report.
A valid `DAILY_DISCORD_WEBHOOK_URL` is needed for report delivery.

### Weekly Report

```powershell
.\.venv\Scripts\python.exe .\src\weekly_report_runner.py
```

This sends the weekly status message through the configured weekly webhook.

## 8. Optional Windows Task Scheduler Setup

1. Open **Task Scheduler**.
2. Choose **Create Basic Task**.
3. Select a daily or weekly trigger.
4. Choose **Start a program**.
5. In **Program/script**, enter the full path to:

   ```text
   <project>\.venv\Scripts\python.exe
   ```

6. In **Add arguments**, enter:

   ```text
   <project>\src\scheduler_runner.py
   ```

7. In **Start in**, enter the project root:

   ```text
   <project>
   ```

For a weekly report task, use `src\weekly_report_runner.py` as the argument.
Using **Start in** is important because the default configuration contains
project-relative paths.

## 9. Testing and Verification

Run the complete test suite:

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

Current verified result:

```text
Ran 20 tests
OK
```

The tests cover:

- file and folder detection and empty input folders;
- valid and invalid module extraction;
- correct movement and automatic folder creation;
- duplicate-safe file and folder names;
- folder movement with preserved contents;
- fallback routing for unknown modules;
- mixed batch processing without data loss;
- GUI selection, Select All, and Deselect All;
- manual, daily, and weekly report routing with mocked network calls.

Detailed test cases, test evidence, and debugging notes are available in
`docs/testing`.

## 10. Troubleshooting

### `Python was not found`

Install Python from [python.org](https://www.python.org/downloads/windows/) and
enable **Add Python to PATH**, then reopen PowerShell.

### PowerShell blocks `Activate.ps1`

Use a temporary policy change for the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Activation is optional. All documented commands can instead use
`.\.venv\Scripts\python.exe` directly.

### `DOWNLOADS_PATH missing in .env`

Create `.env` from `.env.example`, keep it in the project root, and fill in all
four required path variables.

### `Folder does not exist`

Create the folder configured by `DOWNLOADS_PATH`, or correct the path:

```powershell
New-Item -ItemType Directory -Path .\input -Force
```

### `Mapping file not found`

Confirm that `.env` contains:

```env
MAPPING_FILE=./config/module_mapping.json
```

### Files go to unexpected folders

Check:

- that the file or folder name contains an uppercase code such as `M122`;
- that the module exists in `config/module_mapping.json`;
- that the JSON destination path belongs to the current computer;
- that the extension category matches the table above.

### Discord report fails

Sorting remains local even when Discord reporting fails. Confirm that the
correct webhook variable contains a complete Discord webhook URL and that the
computer has internet access. Leave webhook values empty if Discord reporting
is not required.

### Tkinter is unavailable

Reinstall Python using the official Windows installer and ensure the optional
**tcl/tk and IDLE** component is selected.

## 11. Project Structure

```text
file-automation-script/
|-- assets/                     Application icon
|-- config/
|   `-- module_mapping.json     Module and category destinations
|-- docs/
|   |-- design/                 UML diagrams and architecture documents
|   |-- grading/                Project grading sheet
|   |-- requirements/           Original project proposal
|   `-- testing/                Test cases, protocol, and debugging evidence
|-- src/
|   |-- main.py                 Command-line entry point
|   |-- gui.py                  Graphical entry point
|   |-- config.py               Environment and JSON configuration
|   |-- detector.py             Input-folder scanning
|   |-- parser.py               Module extraction
|   |-- mover.py                Destination and movement workflow
|   |-- mover_categories.py     Extension categories
|   |-- mover_filename.py       Duplicate-safe naming
|   |-- logger.py               File logging
|   |-- discord_reporter.py     Discord webhook delivery
|   |-- scheduler_runner.py     Daily scheduled workflow
|   `-- weekly_report_runner.py Weekly report workflow
|-- tests/                      Automated unit tests and fixtures
|-- .env.example                Configuration template
|-- INSTRUCTIONS.md             ZIP installation and user guide
|-- README.md                   Project documentation
`-- requirements.txt            Pinned Python dependencies
```

The `input`, `output`, and `logs` folders are runtime folders and may be created
locally as needed.

## 12. Architecture and Design

The project uses small modules with focused responsibilities:

- **Configuration layer:** loads environment variables and JSON mappings.
- **Detection layer:** reads direct child files and folders from the input folder.
- **Parsing layer:** extracts module identifiers with a regular expression.
- **Movement layer:** resolves destinations, categories, and duplicate names.
- **Presentation layer:** provides the Tkinter user interface.
- **Reporting layer:** writes logs and optionally sends Discord summaries.
- **Automation layer:** exposes daily and weekly scheduler entry points.

This structure follows separation of concerns and makes individual components
easier to test and maintain. The component and activity diagrams are located at:

- `docs/design/diagrams/component_diagram.drawio.png`
- `docs/design/diagrams/activity_diagram.drawio.png`

### Component Diagram

The component diagram shows how the Python modules, configuration files,
filesystem destinations, logs, and optional Discord reporting interact.

![Automated Download Organizer component diagram](docs/design/diagrams/component_diagram.drawio.png)

### Activity Diagram

The activity diagram follows the complete decision flow from configuration and
file detection through parsing, folder creation, duplicate handling, movement,
logging, and reporting.

![Automated Download Organizer activity diagram](docs/design/diagrams/activity_diagram.drawio.png)

## 13. Development Process

The work was organized in project-board phases that mirror the proposal:

- **Design:** folder architecture, parsing, error handling, logging, component
  diagram, and activity diagram.
- **Development:** project setup, monitoring, parsing, mapping, moving,
  configuration, logging, duplicates, reporting, GUI, and refactoring.
- **Testing:** detector, parser, movement, missing folders, duplicates, GUI
  selection, reporting, empty input, unknown modules, and mixed batches.

This progression provides traceability from the initial problem and MoSCoW
requirements to the implemented modules and their automated tests.

## 14. Build an Executable

With the virtual environment active:

```powershell
pyinstaller --onefile --windowed --icon=assets/icon.ico --name="M122 File Organizer" src/gui.py
```

The executable is created in `dist`. The `.env` file and
`config/module_mapping.json` are external configuration files and must remain
available to the application unless they are explicitly bundled through a
custom PyInstaller specification.

## 15. Data Safety

- Files are moved from the source folder; they are not copied.
- Existing destination files are not overwritten.
- Test first with the local `input` folder.
- Keep a backup when evaluating with important documents.
- Review module paths before selecting **Execute Sorting**.
- Keep Discord webhook URLs private.

## Author

Nikola  
GIBZ Informatik  
Module 122 - Automating Processes with a Scripting Language
