# UML Design Documentation

## Overview

This document explains how UML was used to design and structure the Automated Download Organizer project.

The UML diagrams were created to visualize the workflow, system structure, module interactions, and automation logic of the Python application.

The diagrams help improve understanding, maintainability, debugging, and future scalability of the project.

---

# Purpose of UML in this Project

The project uses UML (Unified Modeling Language) to:

- Visualize the automation workflow
- Model the interaction between Python modules
- Document filesystem interactions
- Explain configuration and logging architecture
- Improve maintainability and readability
- Support software engineering best practices

The UML diagrams are part of the required design documentation for Module 122.

---

# Used UML Diagrams

## UML Activity Diagram

The activity diagram models the complete execution workflow of the automation script.

### Purpose

The diagram visualizes:

- Application startup
- Configuration loading
- File detection
- Filename validation
- Module extraction
- Duplicate handling
- File movement
- Logging and error handling
- Application shutdown

### Implemented UML Elements

The activity diagram uses:

- Actions
- Decision nodes
- Loops
- Conditional branches
- Start and end nodes
- Sequential workflow control

### Relation to Python Code

The activity diagram directly reflects the runtime behavior implemented in:

```txt
src/main.py
src/core/detector.py
src/core/parser.py
src/shared/logger.py
src/shared/config.py
```

The workflow is based on the actual automation logic of the application.

---

## UML Component Diagram

The component diagram models the system architecture and module interactions.

### Purpose

The diagram visualizes:

- Python module structure
- Filesystem interactions
- Logging system
- Environment configuration
- Module dependencies
- Folder mappings
- External configuration files

### Components Included

#### Python Modules

- main.py
- detector.py
- parser.py
- logger.py
- config.py

#### Configuration Components

- .env
- module_mapping.json

#### Filesystem Components

- Downloads folder
- Module folders
- Unknown files folder
- Logs folder

### Relation to Python Code

The component diagram represents the modular architecture implemented inside the project source code.

The design follows:

- Separation of concerns
- Modular programming
- Single Responsibility Principle
- Low coupling architecture

---

# UML Design Decisions

## Modular Architecture

The application was divided into separate Python modules to improve:

- Maintainability
- Readability
- Scalability
- Testing
- Reusability

Each module has a dedicated responsibility.

---

## Error Handling Representation

The activity diagram includes multiple decision branches for:

- Invalid filenames
- Missing folders
- Duplicate files
- Configuration problems
- File movement errors

This reflects the implemented error handling strategy of the application.

---

## Logging Integration

Logging is represented in both UML diagrams because logging is a central system component.

The logging system records:

- Information messages
- Warnings
- Errors
- File operations
- Duplicate handling
- Runtime events

---

## Configuration Integration

The UML diagrams include:

- Environment variables
- JSON configuration
- Dynamic folder mappings

This reflects the configurable architecture of the project and avoids hardcoded values.

---

# UML Tools and Technologies

The diagrams were created using:

- PlantUML
- draw.io (diagrams.net)

### Diagram Format

The diagrams are stored as:

```txt
.puml
```

and exported as:

```txt
.png
```

---

# Diagram Storage Structure

```txt
docs/design/
├── diagrams/
│   ├── activity_diagram.puml
│   ├── component_diagram.puml
│   ├── activity_diagram.png
│   └── component_diagram.png
│
└── architecture/
    └── uml_design_documentation.md
```

---

# Benefits of UML for this Project

Using UML provides several advantages:

- Better visualization of workflows
- Easier understanding of system architecture
- Improved documentation quality
- Better maintainability
- Easier debugging and testing
- Clear communication of design decisions

The UML documentation also supports the software engineering requirements of Module 122.

---

# Conclusion

The UML diagrams were designed to accurately represent the real implementation of the Automated Download Organizer project.

The activity diagram models the runtime workflow of the automation process, while the component diagram models the modular architecture and system interactions.

Together, the diagrams improve the clarity, maintainability, and professional quality of the project documentation.
