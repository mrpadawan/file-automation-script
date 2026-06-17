# Installation and User Instructions

This guide explains how to install, configure, and run the M122 File Organizer
on Windows.

## Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer
- Permission to create folders and move files
- Internet connection for the first dependency installation

Discord is optional. The file sorting works without Discord webhooks.

## 1. Extract the Project

Extract the ZIP file to a normal writable folder, for example:

```text
C:\Users\YourName\Documents\M122-File-Organizer
```

Open PowerShell in the extracted project folder. The folder should contain
`README.md`, `requirements.txt`, `src`, `config`, `docs`, and `tests`.

## 2. Create the Python Environment

Run these commands from the project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Optional check:

```powershell
.\.venv\Scripts\python.exe -m pip check
```

Expected result:

```text
No broken requirements found.
```

## 3. Create `.env`

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and use safe test paths first:

```env
DOWNLOADS_PATH=./input
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=./output/unknown
MAPPING_FILE=./config/module_mapping.json

MANUAL_DISCORD_WEBHOOK_URL=
DAILY_DISCORD_WEBHOOK_URL=
WEEKLY_DISCORD_WEBHOOK_URL=
```

Create the input folder:

```powershell
New-Item -ItemType Directory -Path .\input -Force
```

## 4. Configure Module Destinations

Open:

```powershell
notepad .\config\module_mapping.json
```

For a local test, these destinations are enough:

```json
{
    "modules": {
        "M122": "./output/M122",
        "M114": "./output/M114",
        "M293": "./output/M293"
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

Later, replace the module paths with real school folders, for example:

```json
"M122": "C:/Users/YourName/Documents/School/M122"
```

Use forward slashes and keep the JSON syntax valid.

## 5. Run a Safe Test

Create sample files:

```powershell
Set-Content .\input\M122_Test.pdf "test"
Set-Content .\input\M114_Exercise.docx "test"
Set-Content .\input\M293_Example.py "print('test')"
Set-Content .\input\Homework.txt "test"
```

Start the GUI:

```powershell
.\.venv\Scripts\python.exe -m src.gui
```

In the GUI:

1. Click **Scan Files**.
2. Check that the files appear.
3. Select the files that should be moved.
4. Click **Execute Sorting**.
5. Check the `output` folder.

Expected result:

```text
output\M122\Theory\M122_Test.pdf
output\M114\Exercises\M114_Exercise.docx
output\M293\Code\M293_Example.py
output\unknown\Theory\Homework.txt
```

The program moves files. It does not copy them.

## 6. Normal Use

GUI:

```powershell
.\.venv\Scripts\python.exe -m src.gui
```

Command-line sorting:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

Daily scheduled runner:

```powershell
.\.venv\Scripts\python.exe -m src.scheduler.scheduler_runner
```

Weekly Discord report:

```powershell
.\.venv\Scripts\python.exe -m src.scheduler.weekly_report_runner
```

## 7. Use the Real Downloads Folder

Only do this after the safe test works.

Change `.env`:

```env
DOWNLOADS_PATH=C:/Users/YourName/Downloads
DEFAULT_UNKNOWN_PATH=C:/Users/YourName/Documents/School/Unknown
```

Also update all module paths in `config/module_mapping.json`.

Before moving real files:

- check the destination paths;
- keep a backup of important files;
- scan with the GUI first;
- select only files that should be moved.

## 8. Run Automated Tests

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

Expected result:

```text
Ran 24 tests
OK
```

## 9. Optional Task Scheduler Setup

Create a basic task in Windows Task Scheduler.

Program:

```text
C:\full\path\to\project\.venv\Scripts\python.exe
```

Arguments for daily sorting:

```text
-m src.scheduler.scheduler_runner
```

Start in:

```text
C:\full\path\to\project
```

For the weekly report, use this argument:

```text
-m src.scheduler.weekly_report_runner
```

## 10. Troubleshooting

`Python was not found`

Install Python from python.org and enable **Add Python to PATH**.

`DOWNLOADS_PATH missing in .env`

Create `.env` from `.env.example` and fill in all required path variables.

`Folder does not exist`

Create the configured input folder or correct `DOWNLOADS_PATH`.

`Mapping file not found`

Check that `.env` contains:

```env
MAPPING_FILE=./config/module_mapping.json
```

Files go to `unknown`

Check that the filename contains an uppercase module code like `M122`, and that
the module exists in `config/module_mapping.json`.

Discord errors

Discord is optional. Leave webhook values empty if reports are not needed.
