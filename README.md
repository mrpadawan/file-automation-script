# M122 File Organizer

Version: **1.6.0**

License: **MIT**

Python project for Module 122. It automates sorting downloaded school files
into module folders.

For installation, configuration, Discord setup, and daily use, see
[INSTRUCTIONS.md](INSTRUCTIONS.md).

## 1. Introduction and Context

The approved project proposal was **Automated Download Organizer for School**.
School files from Microsoft Teams, GitLab, browsers, and similar platforms
usually land in one Downloads folder. They then have to be moved manually into
module folders such as `M122`, `M114`, or `M293`.

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
- run through the command line, Tkinter GUI, or Windows Task Scheduler;
- optionally send manual, daily, and weekly Discord reports;
- verify behavior with automated unit tests.

Not implemented:

- cloud synchronization such as OneDrive or Google Drive;
- database storage;
- real-time multi-user synchronization;
- continuous background watching without being started manually or by Task
  Scheduler.

The core project is the file-sorting script from the proposal. The Tkinter GUI
is only an optional local helper for scanning, selecting, and starting the same
automation.

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
| Deployment | Optional local execution setup. | GUI, CLI, and Task Scheduler instructions. |

## 5. Design

The project is split into small modules:

- `src/core` scans folders and extracts module codes;
- `src/sorting` decides destinations and moves files/folders;
- `src/shared` loads configuration and logging;
- `src/gui` contains the optional Tkinter interface;
- `src/scheduler` contains automated runner scripts;
- `src/reporting` sends optional Discord webhook reports.

Design documents:

- [Activity diagram](docs/design/diagrams/activity_diagram.drawio.png)
- [Component diagram](docs/design/diagrams/component_diagram.drawio.png)
- [UML design documentation](docs/design/architecture/uml_design_documentation.md)

## 6. Testing

Latest verified result:

```text
Ran 24 tests
OK
```

Testing documentation:

- [Test cases](docs/testing/test_cases.md)
- [Test protocol](docs/testing/test_protocol.md)
- [Debugging notes](docs/testing/debugging.md)

## 7. Screenshot Evidence

| Evidence | Screenshot |
|---|---|
| Empty GUI before scanning | [01-main-window-empty.png](docs/screenshots/01-main-window-empty.png) |
| Input folder before scan | [02-input-folder-before-scan.png](docs/screenshots/02-input-folder-before-scan.png) |
| GUI after scan | [03-gui-after-scan.png](docs/screenshots/03-gui-after-scan.png) |
| GUI file selection | [04-gui-selection.png](docs/screenshots/04-gui-selection.png) |
| GUI after sorting | [05-gui-after-sorting.png](docs/screenshots/05-gui-after-sorting.png) |
| Sorted output folder | [06-output-folder-sorted.png](docs/screenshots/06-output-folder-sorted.png) |
| Duplicate handling | [07-duplicate-handling.png](docs/screenshots/07-duplicate-handling.png) |
| Environment configuration | [08-env-example-config-blurred.png](docs/screenshots/08-env-example-config-blurred.png) |
| Module mapping JSON | [09-module-mapping-json.png](docs/screenshots/09-module-mapping-json.png) |
| Discord daily report | [11-discord-daily-report.png](docs/screenshots/11-discord-daily-report.png) |
| Task Scheduler setup | [12-task-scheduler.png](docs/screenshots/12-task-scheduler.png) |
| Built executable | [13-14-built-executable.png](docs/screenshots/13-14-built-executable.png) |

## 8. Documentation Map

- `README.md`: project overview, requirements, design, testing, and evidence.
- [INSTRUCTIONS.md](INSTRUCTIONS.md): installation, configuration, Discord, and usage.
- `docs/testing`: test cases, protocol, and debugging evidence.
- `docs/design`: UML diagrams and short design explanation.
- `docs/requirements/Official_Project_Proposal.docx`: approved project proposal.

## Author

Nikola  
GIBZ Informatik  
Module 122 - Automating Processes with a Scripting Language
