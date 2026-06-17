# M122 File Organizer

Version: **1.6.0**

License: **MIT**

Python project for Module 122. It automates sorting downloaded school files
into module folders.

## 1. Introduction and Context

The approved project proposal was **Automated Download Organizer for School**.
Every day, school files are downloaded from Microsoft Teams, GitLab, browsers,
and similar platforms. They usually land in one Downloads folder and then have
to be moved manually into module folders such as `M122`, `M114`, or `M293`.

This project automates that task. It scans one configured input folder, reads a
module code from each file or folder name, and moves the item to the configured
module destination.

## 2. Scope

Implemented:

- scan files and direct child folders from `DOWNLOADS_PATH`;
- detect module codes such as `M122` and `M122E`;
- map modules through `config/module_mapping.json`;
- move files into category folders such as `Theory`, `Exercises`, `Code`,
  `Archives`, and `Executables`;
- move folders as complete folders into the module root;
- send unknown or unmapped items to `DEFAULT_UNKNOWN_PATH`;
- create missing destination folders;
- prevent overwrites with `_V2`, `_V3`, and later suffixes;
- write logs to `logs/application.log`;
- run through the command line, a simple Tkinter GUI, or Windows Task Scheduler;
- optionally send manual, daily, and weekly Discord reports;
- verify behavior with automated unit tests.

Not implemented:

- cloud synchronization such as OneDrive or Google Drive;
- database storage;
- real-time multi-user synchronization;
- continuous background watching without being started manually or by Task
  Scheduler.

The core project is still the file-sorting script from the proposal. The
Tkinter GUI is only an optional local helper for scanning, selecting, and
starting the same automation.

## 3. Requirements

### Functional Requirements

| ID | Priority | Requirement | Status |
|---|---|---|---|
| F-01 | Must | Scan a configured input folder. | Done |
| F-02 | Must | Detect module identifiers from names. | Done |
| F-03 | Must | Move items to the correct module folder. | Done |
| F-04 | Must | Create missing folders automatically. | Done |
| F-05 | Should | Log actions and errors. | Done |
| F-06 | Should | Handle duplicate names safely. | Done |
| F-07 | Should | Handle missing or unknown module names. | Done |
| F-08 | Could | Configure module paths with JSON. | Done |
| F-09 | Could | Run automatically with Task Scheduler. | Done |
| F-10 | Could | Send optional Discord reports. | Done |
| F-11 | Won't | Cloud integration. | Not planned |
| F-12 | Won't | Database integration. | Not planned |
| F-13 | Won't | Real-time multi-user use. | Not planned |

### Non-Functional Requirements

| Area | Requirement | Implementation |
|---|---|---|
| Reliability | Existing files must not be overwritten. | Duplicate names receive version suffixes. |
| Usability | A user must be able to install and run the script. | See `INSTRUCTIONS.md`. |
| Maintainability | Code should be split into understandable modules. | `src/core`, `src/sorting`, `src/gui`, `src/scheduler`, `src/reporting`, `src/shared`. |
| Configurability | Paths should not be hardcoded in source code. | `.env` and `module_mapping.json`. |
| Testability | Important behavior must be covered by tests. | 24 unit tests pass. |
| Security | Private webhook URLs should not be committed. | `.env` is ignored by Git. |

## 4. Project Plan

The project followed the waterfall phases required by Module 122.

| Phase | Main Work | Result |
|---|---|---|
| Requirements Analysis | Proposal, MoSCoW requirements, systems involved. | Approved project idea and scope. |
| Design | Folder workflow, module mapping, UML diagrams. | Activity and component diagrams. |
| Development | Detection, parsing, moving, config, logging, GUI, scheduler, reports. | Working Python application. |
| Testing | Unit tests, edge cases, debugging, test protocol. | 24 passing tests and documented results. |
| Deployment | Optional local execution setup. | Instructions for GUI, CLI, and Task Scheduler. |

## 5. Design

The project is split into small modules:

- `src/core` scans folders and extracts module codes;
- `src/sorting` decides destinations and moves files/folders;
- `src/shared` loads configuration and logging;
- `src/gui` contains the optional Tkinter interface;
- `src/scheduler` contains automated runner scripts;
- `src/reporting` sends optional Discord webhook reports.

Design documents:

- `docs/design/diagrams/activity_diagram.drawio.png`
- `docs/design/diagrams/component_diagram.drawio.png`
- `docs/design/architecture/uml_design_documentation.md`

## 6. Configuration

Copy `.env.example` to `.env` and edit the paths:

```env
DOWNLOADS_PATH=./input
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=./output/unknown
MAPPING_FILE=./config/module_mapping.json

MANUAL_DISCORD_WEBHOOK_URL=
DAILY_DISCORD_WEBHOOK_URL=
WEEKLY_DISCORD_WEBHOOK_URL=
```

Configure module destinations in `config/module_mapping.json`:

```json
{
    "modules": {
        "M122": "./output/M122",
        "M114": "./output/M114"
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

Use forward slashes in Windows paths, for example:

```json
"M122": "C:/Users/YourName/Documents/School/M122"
```

## 7. Running the Project

Install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the GUI:

```powershell
.\.venv\Scripts\python.exe -m src.gui
```

Run the command-line sorter:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

Run the daily scheduled workflow manually:

```powershell
.\.venv\Scripts\python.exe -m src.scheduler.scheduler_runner
```

Detailed setup instructions are in `INSTRUCTIONS.md`.

## 8. Testing

Run all tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

Latest verified result:

```text
Ran 24 tests
OK
```

Testing documentation:

- `docs/testing/test_cases.md`
- `docs/testing/test_protocol.md`
- `docs/testing/debugging.md`

## 9. Documentation Map

- `README.md`: main project documentation.
- `INSTRUCTIONS.md`: installation and usage guide.
- `docs/testing`: test cases, protocol, and debugging evidence.
- `docs/design`: UML diagrams and short design explanation.
- `docs/requirements/Official_Project_Proposal.docx`: approved project proposal.

## Author

Nikola  
GIBZ Informatik  
Module 122 - Automating Processes with a Scripting Language
