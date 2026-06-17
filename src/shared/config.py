"""
Application configuration.

Loads:
- Environment variables
- Module mappings
- Subfolder mappings

Validates required configuration
and creates required folders.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


"""
Load configuration values from
environment variables and the
module mapping JSON file.
"""

DOWNLOADS_PATH = os.getenv("DOWNLOADS_PATH")
LOG_PATH = os.getenv("LOG_PATH")
DEFAULT_UNKNOWN_PATH = os.getenv("DEFAULT_UNKNOWN_PATH")
MAPPING_FILE = os.getenv("MAPPING_FILE")
MANUAL_DISCORD_WEBHOOK_URL = os.getenv(
    "MANUAL_DISCORD_WEBHOOK_URL"
)
DAILY_DISCORD_WEBHOOK_URL = os.getenv(
    "DAILY_DISCORD_WEBHOOK_URL"
)
WEEKLY_DISCORD_WEBHOOK_URL = os.getenv(
    "WEEKLY_DISCORD_WEBHOOK_URL"
)

if not DOWNLOADS_PATH:
    raise ValueError(
        "DOWNLOADS_PATH missing in .env"
    )

if not LOG_PATH:
    raise ValueError(
        "LOG_PATH missing in .env"
    )

if not DEFAULT_UNKNOWN_PATH:
    raise ValueError(
        "DEFAULT_UNKNOWN_PATH missing in .env"
    )

if not MAPPING_FILE:
    raise ValueError(
        "MAPPING_FILE missing in .env"
    )


mapping_path = Path(MAPPING_FILE)

if not mapping_path.exists():
    raise FileNotFoundError(
        f"Mapping file not found: {MAPPING_FILE}"
    )


with open(
        mapping_path,
        "r",
        encoding="utf-8-sig"
) as file:

    configuration = json.load(file)

    MODULE_MAPPING = configuration["modules"]

    SUBFOLDER_MAPPING = configuration["subfolders"]


Path(LOG_PATH).mkdir(
    parents=True,
    exist_ok=True
)

Path(DEFAULT_UNKNOWN_PATH).mkdir(
    parents=True,
    exist_ok=True
)
