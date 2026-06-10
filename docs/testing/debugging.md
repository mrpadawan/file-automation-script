# M122 File Organizer - Debugging Evidence

## Debugger Method

The project was debugged with the VS Code Python debugger and the `unittest`
test runner. Breakpoints were placed at decision points where the program
branches or repeats over files, because these locations show whether the
program flow follows the intended logic.

| Area | File | Breakpoint Purpose | Variables Watched |
|---|---|---|---|
| Folder scan loop | `src/detector.py` | Pause inside the `for item in folder.iterdir()` loop to confirm only files are collected and folders/system files are skipped. | `item`, `item.is_file()`, `files` |
| Module parsing | `src/parser.py` | Pause after the regex search to confirm valid filenames return a module and invalid filenames return `None`. | `filename`, `match`, `match.group()` |
| Destination selection | `src/mover.py` | Pause in `determine_destination()` to verify known modules use mapped folders and unknown modules use the fallback path. | `module`, `MODULE_MAPPING`, `DEFAULT_UNKNOWN_PATH` |
| Subfolder selection | `src/mover.py` | Step through extension checks to verify PDFs go to Theory, documents go to Exercises, and code files go to Code. | `extension`, `destination_folder`, `SUBFOLDER_MAPPING` |
| Duplicate handling loop | `src/mover.py` | Pause inside the `while destination_file.exists()` loop to verify `_V2`, `_V3`, and later filenames are generated without overwriting existing files. | `counter`, `destination_file`, `new_name` |
| Discord reporting | `src/discord_reporter.py` | Step into report functions to verify each report type delegates to the correct webhook URL. | `webhook_url`, `message` |

## Error, Warning, and Exception Handling

| Type | Meaning in This Project | Example | Resolution |
|---|---|---|---|
| Error | A problem that prevents correct execution or configuration. | Missing `DOWNLOADS_PATH` in `.env`. | Add the missing environment variable and rerun the program. |
| Warning | A non-fatal situation that should be logged or checked. | A filename does not contain a valid module identifier. | Route the file to the configured fallback destination or leave it unprocessed, depending on workflow. |
| Exception | A Python runtime signal raised when an operation cannot continue normally. | `FileNotFoundError` when the configured scan folder does not exist. | Validate paths before execution and document expected setup. |

## White-Box and Black-Box Testing

White-box testing was used for internal program paths where the code structure is known. Examples include the detector loop, parser branch for valid and invalid module names, duplicate filename loop, and fallback destination branch.

Black-box testing was used from the user's point of view. Examples include selecting files in the GUI, clicking Select All or Deselect All, and confirming that reports are sent through the correct report action.

## Debugging Fixes Confirmed

| Issue Found | Debugging Observation | Fix or Confirmation |
|---|---|---|
| Duplicate files could overwrite previous files if the version loop failed. | The debugger showed `destination_file.exists()` stayed true until a free versioned name was found. | Confirmed by `test_duplicate_handling`. |
| Empty folders needed to be handled without crashing. | Stepping through `scan_folder()` showed the loop completes with no items and returns an empty list. | Confirmed by `test_empty_input_folder`. |
| Unknown modules needed to avoid normal module folders. | Watching `determine_destination()` showed missing mapping keys return `DEFAULT_UNKNOWN_PATH`. | Confirmed by `test_unknown_module_uses_fallback_destination`. |
| Discord tests should not send real network requests. | Debugging confirmed report functions delegate to `_send_message()`. | Confirmed with mocked `_send_message()` in `test_discord.py`. |

## Final Test Command

The final automated test run was executed from the project virtual environment:

```powershell
.venv\Scripts\python.exe -m unittest discover tests
```

Expected result:

```txt
Ran 15 tests
OK
```
