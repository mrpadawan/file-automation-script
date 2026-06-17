# M122 File Organizer - Test Cases

The automated suite contains 24 unit tests. The table below groups them into
the useful test criteria required for the project documentation.

| ID | Area | Test Criteria | Expected Result |
|---|---|---|---|
| TC-01 | Detection | Scan a folder with files and user folders. | Processable files and folders are detected. |
| TC-02 | Detection | Scan an empty folder and a folder with technical items. | Empty folders are handled, and technical folders/files are ignored. |
| TC-03 | Parsing | Parse names such as `M122_Report.pdf`, `M122E_Project`, and `Homework.txt`. | Valid module codes are returned; invalid names return `None`. |
| TC-04 | File movement | Move known module files with different extensions. | Files are moved to the correct module and category folder. |
| TC-05 | Folder creation | Move a file when the destination folder does not exist. | Missing folders are created automatically. |
| TC-06 | Duplicate handling | Move a file or folder when the same name already exists. | Existing items stay unchanged and the new item gets a `_V2` or later suffix. |
| TC-07 | Unknown modules | Move files or folders with no configured module. | Items go to `DEFAULT_UNKNOWN_PATH`. |
| TC-08 | Folder movement | Move a module folder such as `M122E_ProjectFolder`. | The whole folder is moved to the module root and contents are preserved. |
| TC-09 | Batch processing | Process a mixed set of known, unknown, duplicate, code, and theory files. | All items are sorted correctly without data loss. |
| TC-10 | GUI selection | Select one file, select all files, and deselect all files. | The selected item list matches the GUI checkbox state. |
| TC-11 | GUI sorting result | Clear sorted files and show movement summaries. | The GUI keeps unsorted files visible and shows correct result text. |
| TC-12 | Discord reports | Trigger manual, daily, and weekly report functions with mocked webhooks. | Each report uses the correct webhook function without real network calls. |

## Method

White-box tests check internal branches such as parsing, duplicate handling,
fallback routing, and folder creation.

Black-box tests check visible behavior such as GUI selection, sorting results,
and report routing.

Run command:

```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```
