"""
File extension categories.

Responsibilities:
- Store extension lists
- Resolve a file extension to a subfolder key
"""

ARCHIVE_EXTENSIONS = [
    ".zip", ".7z", ".rar", ".tar", ".gz", ".tgz", ".bz2", ".tbz",
    ".tbz2", ".xz", ".txz", ".lz", ".lzma", ".z", ".cab", ".iso",
    ".dmg", ".arj", ".ace", ".cpio", ".wim", ".swm", ".apk", ".ipa",
    ".war", ".ear"
]

EXECUTABLE_EXTENSIONS = [
    ".exe", ".bat", ".cmd", ".msi", ".ps1", ".scr", ".com", ".jar"
]

EXERCISE_EXTENSIONS = [
    ".docx", ".doc", ".odt", ".xlsx", ".xls", ".ods", ".pptx",
    ".ppt", ".odp", ".rtf"
]

THEORY_EXTENSIONS = [
    ".pdf", ".md", ".txt", ".epub"
]

CODE_EXTENSIONS = [
    ".py", ".cs", ".java", ".js", ".ts", ".html", ".css", ".cpp",
    ".c", ".h", ".hpp", ".sql", ".php", ".go", ".rs", ".kt",
    ".swift", ".sh", ".ps1", ".vb", ".json", ".xml", ".yaml", ".yml"
]


def get_subfolder_key(extension):
    """
    Return the matching subfolder key
    for a file extension.

    Args:
        extension (str):
            File extension.

    Returns:
        str | None:
            Subfolder mapping key or
            None when no category matches.
    """

    if extension in EXERCISE_EXTENSIONS:
        return "exercise"

    if extension in ARCHIVE_EXTENSIONS:
        return "archives"

    if extension in EXECUTABLE_EXTENSIONS:
        return "executables"

    if extension in THEORY_EXTENSIONS:
        return "theory"

    if extension in CODE_EXTENSIONS:
        return "code"

    return None
