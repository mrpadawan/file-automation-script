# UML Design Documentation

This document explains the two UML diagrams used for the M122 File Organizer.
The diagrams support the design part of the Module 122 project documentation.

## Activity Diagram

File:

```text
docs/design/diagrams/activity_diagram.drawio.png
```

Purpose:

- show the main workflow from start to finish;
- show configuration loading;
- show scanning, module parsing, destination selection, duplicate handling, and
  file movement;
- show where errors and unknown modules are handled.

Related code:

- `src/main.py`
- `src/core/detector.py`
- `src/core/parser.py`
- `src/sorting/mover.py`
- `src/shared/config.py`
- `src/shared/logger.py`

## Component Diagram

File:

```text
docs/design/diagrams/component_diagram.drawio.png
```

Purpose:

- show the main Python packages;
- show the connection to `.env`;
- show the connection to `config/module_mapping.json`;
- show filesystem input, module destinations, fallback folder, and logs;
- show optional Discord reporting.

Related packages:

- `src/core`
- `src/sorting`
- `src/shared`
- `src/gui`
- `src/scheduler`
- `src/reporting`

## Design Decisions

- Configuration is outside the source code in `.env` and JSON.
- File scanning, parsing, moving, logging, GUI, and reporting are separated into
  different modules.
- Duplicate handling is implemented before moving files so existing files are
  not overwritten.
- Unknown files are not deleted. They are moved to the configured fallback
  folder.
- The GUI is optional. The command-line workflow remains available.

## Diagram Files

```text
docs/design/diagrams/activity_diagram.drawio
docs/design/diagrams/activity_diagram.drawio.png
docs/design/diagrams/activity_diagram.puml
docs/design/diagrams/component_diagram.drawio
docs/design/diagrams/component_diagram.drawio.png
docs/design/diagrams/component_diagram.puml
```
