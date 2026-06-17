"""
Unit tests for Discord reporting functionality.
"""

import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


class TestDiscordReporter(unittest.TestCase):
    """
    Validates that manual, daily, and weekly Discord report functions delegate
    messages to the configured webhook delivery mechanism.
    """

    def setUp(self):
        """
        Configure isolated environment values required by the reporting module.
        """

        self.temporary_directory = tempfile.TemporaryDirectory()
        workspace = Path(self.temporary_directory.name)
        mapping_file = workspace / "module_mapping.json"
        mapping_file.write_text(
            '{"modules": {}, "subfolders": {"exercise": "Exercises", "theory": "Theory", "code": "Code"}}',
            encoding="utf-8"
        )

        os.environ["DOWNLOADS_PATH"] = str(workspace / "input")
        os.environ["LOG_PATH"] = str(workspace / "logs")
        os.environ["DEFAULT_UNKNOWN_PATH"] = str(workspace / "unknown")
        os.environ["MAPPING_FILE"] = str(mapping_file)
        os.environ["MANUAL_DISCORD_WEBHOOK_URL"] = "https://example.com/manual"
        os.environ["DAILY_DISCORD_WEBHOOK_URL"] = "https://example.com/daily"
        os.environ["WEEKLY_DISCORD_WEBHOOK_URL"] = "https://example.com/weekly"

        from src.shared import config
        from src.reporting import discord_reporter

        importlib.reload(config)
        self.discord_reporter = importlib.reload(discord_reporter)

    def tearDown(self):
        """
        Remove isolated reporting configuration after each test.
        """

        self.temporary_directory.cleanup()

    @patch("src.reporting.discord_reporter._send_message")
    def test_manual_report(self, mocked_send_message):
        """
        Verify that a manual report uses the manual Discord webhook endpoint.
        """

        self.discord_reporter.send_manual_report("Manual report")

        mocked_send_message.assert_called_once_with(
            "https://example.com/manual",
            "Manual report"
        )

    @patch("src.reporting.discord_reporter._send_message")
    def test_daily_report(self, mocked_send_message):
        """
        Verify that a daily report uses the daily Discord webhook endpoint.
        """

        self.discord_reporter.send_daily_report("Daily report")

        mocked_send_message.assert_called_once_with(
            "https://example.com/daily",
            "Daily report"
        )

    @patch("src.reporting.discord_reporter._send_message")
    def test_weekly_report(self, mocked_send_message):
        """
        Verify that a weekly report uses the weekly Discord webhook endpoint.
        """

        self.discord_reporter.send_weekly_report("Weekly report")

        mocked_send_message.assert_called_once_with(
            "https://example.com/weekly",
            "Weekly report"
        )


if __name__ == "__main__":
    unittest.main()
