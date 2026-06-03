"""
Application logging configuration.

Creates application log files
and provides centralized logging.

Note:
    This module initializes the
    logging system once and exposes
    a shared logger instance that
    can be used throughout the
    application.
"""

import logging
from config import LOG_PATH


logging.basicConfig(
    filename=f"{LOG_PATH}/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger()