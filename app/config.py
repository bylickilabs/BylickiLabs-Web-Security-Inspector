from __future__ import annotations

from pathlib import Path

APP_NAME = "BylickiLabs Web Security Inspector"
APP_TITLE = "Enterprise Website Security Analytics"
APP_VERSION = "2.0.0"
APP_AUTHOR = "Thorsten Bylicki | BylickiLabs"
APP_DESCRIPTION = (
    "Bilingual desktop application for structured website security, configuration, "
    "performance and statistical analysis."
)
APP_COPYRIGHT = "Copyright © 2026 Thorsten Bylicki | BylickiLabs"
APP_LICENSE = "MIT"
GITHUB_URL = ""

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
DATABASE_PATH = DATA_DIR / "scan_history.sqlite3"
SETTINGS_PATH = DATA_DIR / "settings.json"

DEFAULT_TIMEOUT = 12
DEFAULT_SAMPLE_COUNT = 3
MAX_RESPONSE_BYTES = 2_000_000
USER_AGENT = f"{APP_NAME}/{APP_VERSION} (+{GITHUB_URL})"

SEVERITY_WEIGHTS = {
    "Critical": 10.0,
    "High": 7.0,
    "Medium": 4.0,
    "Low": 1.5,
    "Info": 0.0,
}
SEVERITY_ORDER = ["Critical", "High", "Medium", "Low", "Info"]
CONFIDENCE_ORDER = ["High", "Medium", "Low"]

for directory in (DATA_DIR, REPORTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)