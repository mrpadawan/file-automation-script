# M122 File Organizer - Test Protocol

Command:

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

Latest execution:

```text
Ran 24 tests
OK
```

Date: 2026-06-17

Tester: Nikola

## Result Table

| ID | Area | Result | Status |
|---|---|---|---|
| TC-01 | Detection of files and folders | Files and direct child folders were detected. | PASS |
| TC-02 | Empty and technical items | Empty input returned no items; technical items were ignored. | PASS |
| TC-03 | Module parsing | Valid module names returned module codes; invalid names returned `None`. | PASS |
| TC-04 | File movement | Files moved to the expected module and category folders. | PASS |
| TC-05 | Folder creation | Missing target folders were created automatically. | PASS |
| TC-06 | Duplicate handling | Duplicate files and folders received version suffixes. | PASS |
| TC-07 | Unknown modules | Unknown items used the fallback destination. | PASS |
| TC-08 | Folder movement | Folders moved as complete units and kept their contents. | PASS |
| TC-09 | Batch processing | Mixed file sets were processed without data loss. | PASS |
| TC-10 | GUI selection | Select, select all, and deselect all behaved correctly. | PASS |
| TC-11 | GUI sorting result | Sorted files were cleared correctly and summaries were accurate. | PASS |
| TC-12 | Discord reports | Manual, daily, and weekly report routing passed with mocked calls. | PASS |

## Evidence Files

- `tests/test_detector.py`
- `tests/test_parser.py`
- `tests/test_mover.py`
- `tests/test_mover_batch.py`
- `tests/test_gui.py`
- `tests/test_discord.py`
