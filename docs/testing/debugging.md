# M122 File Organizer - Debugging Notes

The project was debugged with the VS Code Python debugger and the `unittest`
runner. Breakpoints were placed where the program makes important decisions.

## Breakpoints Used

| Area | File | What Was Checked |
|---|---|---|
| Folder scan | `src/core/detector.py` | Files and user folders are collected, technical items are skipped. |
| Module parsing | `src/core/parser.py` | Valid names return a module code, invalid names return `None`. |
| Destination selection | `src/sorting/mover.py` | Known modules use mapped folders; unknown modules use fallback. |
| Category selection | `src/sorting/mover.py` | Extensions are routed to the expected subfolder. |
| Duplicate handling | `src/sorting/mover_filename.py` | `_V2`, `_V3`, and later suffixes are created safely. |
| Reporting | `src/reporting/discord_reporter.py` | Manual, daily, and weekly reports use the correct webhook setting. |

## Error Handling Checked

| Situation | Expected Handling |
|---|---|
| Missing input folder | Raise a clear `FileNotFoundError`. |
| Missing `.env` value | Raise a clear configuration error. |
| Missing mapping file | Raise a clear `FileNotFoundError`. |
| Unknown module name | Move to `DEFAULT_UNKNOWN_PATH`. |
| Duplicate destination name | Keep the existing item and rename the new one. |
| Discord failure | Local sorting is not controlled by Discord. |

## Confirmed Fixes

- Duplicate files and folders do not overwrite existing items.
- Empty input folders do not crash the scanner.
- Unknown modules use the fallback folder.
- Folder moves preserve folder contents.
- Discord tests use mocked webhook calls instead of real network requests.

Final verification command:

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

Final result:

```text
Ran 24 tests
OK
```
