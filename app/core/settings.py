from __future__ import annotations

import json
from dataclasses import asdict, dataclass

from app.config import DEFAULT_SAMPLE_COUNT, DEFAULT_TIMEOUT, SETTINGS_PATH


@dataclass(slots=True)
class AppSettings:
    language: str = "de"
    theme: str = "dark"
    timeout_seconds: int = DEFAULT_TIMEOUT
    sample_count: int = DEFAULT_SAMPLE_COUNT
    verify_tls: bool = True
    enable_observatory: bool = False
    enable_pagespeed: bool = False
    pagespeed_api_key: str = ""
    save_history: bool = True

    def save(self) -> None:
        SETTINGS_PATH.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")

    @classmethod
    def load(cls) -> "AppSettings":
        if not SETTINGS_PATH.exists():
            return cls()
        try:
            data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
            allowed = cls.__dataclass_fields__.keys()
            return cls(**{key: value for key, value in data.items() if key in allowed})
        except (OSError, ValueError, TypeError):
            return cls()
