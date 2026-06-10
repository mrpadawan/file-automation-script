# M122 File Organizer - Test Protocol

Test execution reference: `.venv\Scripts\python.exe -m unittest discover tests`  
Execution result: `Ran 15 tests - OK`

## Evidence Files

| Evidence | Purpose |
|---|---|
| `tests/test_detector.py` | Automated tests for file detection, ignored folders, and empty input folders. |
| `tests/test_parser.py` | Automated tests for valid and invalid module extraction. |
| `tests/test_mover.py` | Automated tests for moving, folder creation, duplicate handling, and fallback routing. |
| `tests/test_gui.py` | Automated tests for GUI selection logic. |
| `tests/test_discord.py` | Automated tests for manual, daily, and weekly Discord report routing with mocked network calls. |
| `docs/testing/debugging.md` | Debugging evidence, breakpoints, watched variables, and white-box/black-box explanation. |

| Test ID | Date | Tester | Expected Result | Actual Result | Status | Notes |
|---|---|---|---|---|---|---|
| TC-001 | 2026-06-07 | Nikola | Files in the input folder are detected, and folders are ignored. | File detection test passed successfully. | PASS | Covered by `test_file_detection`. |
| TC-002 | 2026-06-07 | Nikola | Parser returns `M122` for a valid module filename. | Valid module extraction returned the expected module identifier. | PASS | Covered by `test_valid_module`. |
| TC-003 | 2026-06-07 | Nikola | Parser returns `None` for a filename without a valid module identifier. | Invalid module extraction returned `None`. | PASS | Covered by `test_invalid_module`. |
| TC-004 | 2026-06-07 | Nikola | File is moved to the configured module destination. | File was moved successfully into the expected module/category folder. | PASS | Covered by `test_file_move`. |
| TC-005 | 2026-06-07 | Nikola | Missing module and category folders are created automatically. | Missing destination folders were created and the file was moved successfully. | PASS | Covered by `test_missing_folder_creation`. |
| TC-006 | 2026-06-07 | Nikola | Duplicate files are renamed without overwriting existing files. | Duplicate file was renamed with `_V2`, and the original file remained unchanged. | PASS | Covered by `test_duplicate_handling`. |
| TC-007 | 2026-06-07 | Nikola | Only individually selected files are included for processing. | Selected checkbox state returned only the selected file. | PASS | Covered by `test_file_selection`. |
| TC-008 | 2026-06-07 | Nikola | Select All selects every displayed file checkbox. | All displayed checkbox states were set to selected. | PASS | Covered by `test_select_all`. |
| TC-009 | 2026-06-07 | Nikola | Deselect All clears every displayed file checkbox. | All displayed checkbox states were set to deselected. | PASS | Covered by `test_deselect_all`. |
| TC-010 | 2026-06-07 | Nikola | Manual report is sent to the configured manual Discord webhook. | Manual report delegated to the configured manual webhook endpoint. | PASS | Covered by `test_manual_report`; webhook call was mocked. |
| TC-011 | 2026-06-07 | Nikola | Daily report is sent to the configured daily Discord webhook. | Daily report delegated to the configured daily webhook endpoint. | PASS | Covered by `test_daily_report`; webhook call was mocked. |
| TC-012 | 2026-06-07 | Nikola | Weekly report is sent to the configured weekly Discord webhook. | Weekly report delegated to the configured weekly webhook endpoint. | PASS | Covered by `test_weekly_report`; webhook call was mocked. |
| TC-013 | 2026-06-10 | Nikola | Empty input folder returns no files and does not cause an application error. | Empty input folder returned an empty list without raising an exception. | PASS | Covered by `test_empty_input_folder`. |
| TC-014 | 2026-06-10 | Nikola | Unknown module files are routed to the configured fallback destination. | Unknown module file was moved to the configured fallback destination. | PASS | Covered by `test_unknown_module_uses_fallback_destination`. |
| TC-015 | 2026-06-10 | Nikola | Large file set is processed accurately without data loss. | Mixed file batch processed successfully; duplicates, known modules, unknown modules, code files, and theory files were moved without data loss. | PASS | Covered by `test_large_mixed_file_set`. |
