# Installation and User Instructions

This guide is written for a teacher, evaluator, or user who received the
project as a ZIP file and wants to run it on a Windows computer.

## Quick Navigation

- [Before You Start](#before-you-start)
- [Extract and Install](#step-1-extract-the-zip-file)
- [Create the Environment](#step-4-create-the-virtual-environment)
- [Configure the Project](#step-6-create-the-local-configuration)
- [Run a Safe Test](#step-8-run-a-safe-test)
- [Run Automated Tests](#step-9-run-the-automated-tests)
- [Use the Real Downloads Folder](#step-10-use-the-real-downloads-folder)
- [Troubleshooting Checklist](#troubleshooting-checklist)
- [Final Verification Checklist](#final-verification-checklist)

## What the Program Does

The M122 File Organizer scans one configured folder and moves its files into
school module folders. A filename containing `M122`, for example, is sent to
the configured M122 destination. The extension then determines whether it goes
into `Exercises`, `Theory`, `Code`, `Archives`, or `Executables`.

The program protects existing files by adding `_V2`, `_V3`, and later suffixes.
Files with an unknown module, or no module code, go to the configured fallback
folder.

## Before You Start

You need:

- Windows 10 or Windows 11;
- permission to create folders and move files;
- Python 3.10 or newer;
- an internet connection for the first dependency installation;
- the extracted project folder.

Discord is optional. No Discord account or webhook is needed for local file
sorting.

## Step 1: Extract the ZIP File

1. Right-click the downloaded ZIP file.
2. Select **Extract All**.
3. Choose a normal writable location, for example:

   ```text
   C:\Users\YourName\Documents\M122-File-Organizer
   ```

4. Open the extracted folder.
5. Confirm that it contains `README.md`, `requirements.txt`, `src`, `config`,
   `docs`, and `tests`.

Do not run the project from inside the ZIP preview. It must be extracted first.

## Step 2: Install Python

1. Download Python from:
   [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Start the installer.
3. Enable **Add Python to PATH**.
4. Keep **pip** and **tcl/tk and IDLE** selected.
5. Complete the installation.
6. Close and reopen PowerShell.

Verify the installation:

```powershell
py --version
```

The command should display Python 3.10 or newer.

## Step 3: Open PowerShell in the Project Folder

In File Explorer:

1. Open the extracted project folder.
2. Click the address bar.
3. Type `powershell`.
4. Press Enter.

The PowerShell prompt should now point to the folder containing
`requirements.txt`.

You can confirm this with:

```powershell
Get-ChildItem
```

## Step 4: Create the Virtual Environment

Run:

```powershell
py -m venv .venv
```

This creates an isolated Python environment inside `.venv`, so the project
dependencies do not interfere with other Python projects.

Activate it:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The execution-policy change only applies to the current PowerShell window.
After activation, the prompt normally begins with `(.venv)`.

## Step 5: Install All Dependencies

Run:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Wait until the installation finishes without an error.

To verify the environment:

```powershell
python -m pip check
```

Expected result:

```text
No broken requirements found.
```

## Step 6: Create the Local Configuration

Copy the template:

```powershell
Copy-Item .env.example .env
```

Open `.env` in Notepad:

```powershell
notepad .env
```

For a safe first test, replace its contents with:

```env
DOWNLOADS_PATH=./input
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=./output/unknown
MAPPING_FILE=./config/module_mapping.json

MANUAL_DISCORD_WEBHOOK_URL=
DAILY_DISCORD_WEBHOOK_URL=
WEEKLY_DISCORD_WEBHOOK_URL=
```

Save and close the file.

Create the test input folder:

```powershell
New-Item -ItemType Directory -Path .\input -Force
```

### Meaning of the Settings

| Setting | Meaning |
|---|---|
| `DOWNLOADS_PATH` | Folder that the application scans. |
| `LOG_PATH` | Folder used for `application.log`. |
| `DEFAULT_UNKNOWN_PATH` | Destination for files without a configured module. |
| `MAPPING_FILE` | JSON file containing module destinations. |
| Discord webhook variables | Optional report destinations; they may remain empty. |

## Step 7: Configure Module Destinations

The supplied `config/module_mapping.json` contains paths from the developer's
computer. They will not be appropriate for another user.

Open the file:

```powershell
notepad .\config\module_mapping.json
```

For a self-contained first test, use:

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

Save and close the file.

Later, each destination can be changed to a real school folder:

```json
"M122": "C:/Users/YourName/Documents/School/M122"
```

Use forward slashes and keep the JSON syntax valid. The program creates missing
destination folders automatically.

## Step 8: Run a Safe Test

Create sample files:

```powershell
Set-Content .\input\M122_Test.pdf "Test PDF content"
Set-Content .\input\M114_Exercise.docx "Test document content"
Set-Content .\input\M293_Example.py "print('test')"
Set-Content .\input\Homework.txt "Unknown module test"
```

These are simple test files used to verify movement; they are not intended to
open as real PDF or Word documents.

Start the GUI:

```powershell
.\.venv\Scripts\python.exe -m src.gui
```

In the application:

1. Click **Scan Files**.
2. Confirm that four files are detected.
3. Click **Select All**.
4. Click **Execute Sorting**.
5. Wait for the finished status.
6. Close the GUI.

Inspect the results:

```powershell
Get-ChildItem .\output -Recurse
```

Expected destinations:

```text
output\M122\Theory\M122_Test.pdf
output\M114\Exercises\M114_Exercise.docx
output\M293\Code\M293_Example.py
output\unknown\Theory\Homework.txt
```

The original files should no longer be inside `input`, because the application
moves files rather than copying them.

## Step 9: Run the Automated Tests

Run:

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

Expected result:

```text
...............
----------------------------------------------------------------------
Ran 15 tests

OK
```

The exact runtime may differ. `OK` confirms that the automated suite passed.

## Step 10: Use the Real Downloads Folder

Only do this after the safe test works.

Open `.env`:

```powershell
notepad .env
```

Change `DOWNLOADS_PATH` to the actual Windows Downloads folder:

```env
DOWNLOADS_PATH=C:/Users/YourName/Downloads
```

Change `DEFAULT_UNKNOWN_PATH` to a real fallback folder:

```env
DEFAULT_UNKNOWN_PATH=C:/Users/YourName/Documents/School/Unknown
```

Update every module destination in `config/module_mapping.json`.

Before processing real files:

1. Check that each module path is correct.
2. Make sure important files are backed up.
3. Start the GUI.
4. Scan and review the list.
5. Select only the files that should be moved.
6. Execute sorting.

## Normal Daily Use

Open PowerShell in the project folder and run:

```powershell
.\.venv\Scripts\python.exe -m src.gui
```

Then:

1. Click **Scan Files**.
2. Review the checkboxes.
3. Select the required files.
4. Click **Execute Sorting**.
5. Review the result.

Virtual-environment activation is not required when the full
`.\.venv\Scripts\python.exe` path is used.

## Command-Line Use

To process every detected file without the GUI:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

This performs one scan and then exits.

## Optional Discord Configuration

Discord webhooks can receive manual, daily, and weekly reports.

1. Create the required webhook in the selected Discord server/channel.
2. Copy its full URL.
3. Open `.env`.
4. Add it to the appropriate setting:

   ```env
   MANUAL_DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
   DAILY_DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
   WEEKLY_DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
   ```

5. Save `.env`.

Webhook URLs are private credentials. Do not include a real URL in screenshots,
GitHub commits, or submitted public documentation.

## Optional Windows Task Scheduler

The application can run automatically at a chosen time.

### Daily Sorting Task

1. Open **Task Scheduler** from the Start menu.
2. Select **Create Basic Task**.
3. Name it `M122 File Organizer Daily`.
4. Choose the desired daily trigger.
5. Choose **Start a program**.
6. In **Program/script**, browse to:

   ```text
   C:\full\path\to\project\.venv\Scripts\python.exe
   ```

7. In **Add arguments**, enter:

   ```text
   -m src.scheduler.scheduler_runner
   ```

8. In **Start in**, enter:

   ```text
   C:\full\path\to\project
   ```

9. Finish and test the task manually.

The scheduled runner processes all files and uses
`DAILY_DISCORD_WEBHOOK_URL` for its report.

### Weekly Report Task

Repeat the steps above, but use:

```text
-m src.scheduler.weekly_report_runner
```

and configure `WEEKLY_DISCORD_WEBHOOK_URL`.

## Logs and Results

The application log is stored at:

```text
logs\application.log
```

View its latest entries:

```powershell
Get-Content .\logs\application.log -Tail 30
```

Moved files are stored in the destinations from
`config/module_mapping.json`, grouped by their extension category.

## Duplicate File Behavior

The application never intentionally overwrites an existing destination file.

Example:

```text
M122_Report.pdf
M122_Report_V2.pdf
M122_Report_V3.pdf
```

The next available suffix is selected automatically.

## Troubleshooting Checklist

### The GUI does not open

Run it with console output visible:

```powershell
.\.venv\Scripts\python.exe -m src.gui
```

Read the displayed error. Then check that Python, dependencies, `.env`, and the
mapping file are available.

### `No module named ...`

Install the requirements again with the virtual environment's Python:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### `.env` values are reported missing

Confirm that the file is named exactly `.env`, not `.env.txt`, and is stored
next to `README.md`.

In File Explorer, enable **View > Show > File name extensions** to check the
real filename.

### The input folder does not exist

Create it or correct `DOWNLOADS_PATH`:

```powershell
New-Item -ItemType Directory -Path .\input -Force
```

### The mapping file cannot be found

Use this value in `.env`:

```env
MAPPING_FILE=./config/module_mapping.json
```

Always launch the program from the project root.

### Files are moved to `unknown`

Check that:

- the filename contains uppercase `M` followed by digits;
- the intended module is present in `config/module_mapping.json`;
- the JSON was saved without syntax errors.

### A destination path is wrong

Stop processing, close the program, and correct
`config/module_mapping.json`. Existing moved files must be moved back manually
if they were sent to a valid but unintended path.

### Discord shows an error

Discord is optional and does not control the local movement logic. Check the
webhook URL and internet connection, or leave the webhook fields empty.

## Clean Reinstallation

If the virtual environment becomes damaged, close the GUI and run:

```powershell
Remove-Item -Recurse -Force .\.venv
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

This recreates only the Python environment. It does not delete `.env`,
configuration, source code, logs, or organized files.

## Final Verification Checklist

Before evaluating or using the project, confirm:

- [ ] The ZIP was extracted.
- [ ] Python 3.10 or newer is installed.
- [ ] `.venv` was created.
- [ ] `requirements.txt` installed successfully.
- [ ] `.env` exists in the project root.
- [ ] `DOWNLOADS_PATH` points to an existing folder.
- [ ] `config/module_mapping.json` contains paths for this computer.
- [ ] The GUI opens.
- [ ] The safe sample test moves files correctly.
- [ ] All 15 automated tests pass.
- [ ] Real files and destinations were reviewed before daily use.

For architecture, features, project context, testing coverage, and design
decisions, see [README.md](README.md).
