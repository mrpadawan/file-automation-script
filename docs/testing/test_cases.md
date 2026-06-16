# M122 File Organizer - Test Cases

| Test ID | Feature | Description | Preconditions | Test Steps | Expected Result |
|---|---|---|---|---|---|
| TC-001 | File and Folder Detection | Verify that files and direct child folders in the configured input folder are detected correctly. | The input folder exists and contains at least one file and one user folder. | 1. Start the detection process.<br>2. Scan the configured input folder.<br>3. Review the detected item list. | Files and folders located directly in the input folder are detected, while technical folders are ignored. |
| TC-002 | Valid Module Extraction | Verify that a valid module identifier is extracted from a filename. | A file named `M122_ProjectDocumentation.pdf` is available. | 1. Pass the filename to the parser.<br>2. Execute module extraction.<br>3. Review the returned module identifier. | The parser returns `M122`. |
| TC-003 | Invalid Module Extraction | Verify that filenames without a valid module identifier are handled correctly. | A file named `ProjectDocumentation.pdf` is available. | 1. Pass the filename to the parser.<br>2. Execute module extraction.<br>3. Review the returned value. | The parser returns `None` and does not assign an incorrect module. |
| TC-004 | File Move | Verify that a file is moved to the correct module destination. | The input folder contains `M122_Report.pdf`, and the module mapping contains `M122`. | 1. Select the file for processing.<br>2. Execute the move operation.<br>3. Inspect the target module folder. | The file is moved from the input folder to the correct `M122` destination folder. |
| TC-005 | Missing Folder Creation | Verify that missing destination folders are created automatically. | The input folder contains `M114_Exercise.docx`, and the `M114` destination folder does not exist. | 1. Select the file for processing.<br>2. Execute the move operation.<br>3. Inspect the output directory structure. | The required module and category folders are created, and the file is moved successfully. |
| TC-006 | Duplicate Handling | Verify that duplicate filenames do not overwrite existing files. | The target folder already contains `M122_Report.pdf`, and the input folder contains another file with the same name. | 1. Select the duplicate file.<br>2. Execute the move operation.<br>3. Inspect the target folder. | The existing file remains unchanged, and the moved file is renamed using the `_V2`, `_V3`, or next available version suffix. |
| TC-007 | GUI File Selection | Verify that individual files can be selected using GUI checkboxes. | The GUI displays at least two detected files. | 1. Select one file checkbox.<br>2. Leave another file checkbox unselected.<br>3. Inspect the selected file list. | Only the checked file is selected for processing. |
| TC-008 | Select All | Verify that the Select All button selects every displayed file. | The GUI displays multiple unchecked files. | 1. Click Select All.<br>2. Inspect all visible file checkboxes.<br>3. Review the selection statistics. | Every displayed file checkbox is selected, and the selection statistics are refreshed. |
| TC-009 | Deselect All | Verify that the Deselect All button clears every displayed file selection. | The GUI displays multiple selected files. | 1. Click Deselect All.<br>2. Inspect all visible file checkboxes.<br>3. Review the selection statistics. | Every displayed file checkbox is deselected, and the selection statistics are refreshed. |
| TC-010 | Manual Discord Report | Verify that a manual Discord report is sent through the configured manual webhook. | A manual Discord webhook URL is configured. | 1. Trigger a manual report.<br>2. Inspect the report delivery call.<br>3. Verify the submitted message content. | A manual report message is sent to the configured manual Discord endpoint. |
| TC-011 | Daily Discord Report | Verify that a daily Discord report is sent through the configured daily webhook. | A daily Discord webhook URL is configured. | 1. Trigger the daily report workflow.<br>2. Inspect the report delivery call.<br>3. Verify the submitted message content. | A daily report message is sent to the configured daily Discord endpoint. |
| TC-012 | Weekly Discord Report | Verify that a weekly Discord report is sent through the configured weekly webhook. | A weekly Discord webhook URL is configured. | 1. Trigger the weekly report workflow.<br>2. Inspect the report delivery call.<br>3. Verify the submitted message content. | A weekly report message is sent to the configured weekly Discord endpoint. |
| TC-013 | Empty Input Folder | Verify that an empty input folder is handled gracefully. | The configured input folder exists and contains no files. | 1. Start the file detection process.<br>2. Scan the input folder.<br>3. Review the application status. | No files are returned, no exception occurs, and the user receives an appropriate status message where applicable. |
| TC-014 | Unknown Module | Verify that an unknown module identifier is routed to the configured fallback destination. | The input folder contains a file such as `M999_Notes.pdf`, and `M999` is not configured in the module mapping. | 1. Extract the module identifier.<br>2. Execute the move operation.<br>3. Inspect the fallback destination. | The file is moved to the configured unknown-module destination without disrupting other files. |
| TC-015 | Large File Set | Verify that the application can process a large number of files reliably. | The input folder contains a large dataset of valid, invalid, duplicate, and unknown-module files. | 1. Scan the input folder.<br>2. Select all detected files.<br>3. Execute the organization process.<br>4. Review output folders, progress behavior, and logs. | The application processes the file set accurately, handles duplicates correctly, and completes without data loss. |
| TC-016 | Folder Detection | Verify that user folders appear as processable items. | The input folder contains `M122E_ProjectFolder`. | 1. Scan the input folder.<br>2. Review the detected item list. | The folder appears in the detected items and can be selected. |
| TC-017 | Folder Move | Verify that a folder is moved to the correct module root folder. | The input folder contains `M122E_ProjectFolder`, and the module mapping contains `M122`. | 1. Select the folder for processing.<br>2. Execute the move operation.<br>3. Inspect the target module folder. | The whole folder is moved into the module destination root, not into a category subfolder. |
| TC-018 | Duplicate Folder Handling | Verify that duplicate folder names do not overwrite existing folders. | The target folder already contains `M122_Project`, and the input folder contains another folder with the same name. | 1. Select the duplicate folder.<br>2. Execute the move operation.<br>3. Inspect the target folder. | The existing folder remains unchanged, and the moved folder is renamed using `_V2`, `_V3`, or the next available suffix. |

## Testing Methodology

The test set combines white-box and black-box testing.

White-box tests check internal code paths and branches:

| Code Path | Covered By |
|---|---|
| Folder iteration returns direct child files and folders. | `test_file_detection` |
| Technical folders are ignored. | `test_technical_folder_ignored` |
| Empty folder loop returns an empty result. | `test_empty_input_folder` |
| Parser returns a module when the regex matches. | `test_valid_module` |
| Parser returns a module with suffix from a folder name. | `test_folder_module_with_suffix` |
| Parser returns `None` when the regex does not match. | `test_invalid_module` |
| Destination folders are created before moving. | `test_missing_folder_creation` |
| Duplicate filename loop generates a safe versioned filename. | `test_duplicate_handling` |
| Folders move into module roots and keep contents. | `test_folder_move_preserves_contents` |
| Duplicate folders receive a safe versioned name. | `test_duplicate_folder_handling` |
| Unknown module branch uses the fallback destination. | `test_unknown_module_uses_fallback_destination` |

Black-box tests check user-visible behavior:

| User Behavior | Covered By |
|---|---|
| Select one file in the GUI. | `test_file_selection` |
| Select all visible files. | `test_select_all` |
| Deselect all visible files. | `test_deselect_all` |
| Send manual, daily, and weekly reports. | `test_manual_report`, `test_daily_report`, `test_weekly_report` |

The executed automated suite covers normal cases, missing values, invalid values, duplicate files and folders, fallback routing, mixed batch processing, and GUI/reporting behavior.
