from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from app.config import DATABASE_PATH
from app.models import ScanResult


class ScanDatabase:
    def __init__(self, path: Path = DATABASE_PATH) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._initialise()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialise(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS scans (
                    scan_id TEXT PRIMARY KEY,
                    target TEXT NOT NULL,
                    profile TEXT NOT NULL,
                    started_at TEXT NOT NULL,
                    completed_at TEXT NOT NULL,
                    duration_seconds REAL NOT NULL,
                    risk_score REAL NOT NULL,
                    grade TEXT NOT NULL,
                    finding_count INTEGER NOT NULL,
                    payload_json TEXT NOT NULL
                )
                """
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_scans_target ON scans(target)"
            )
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_scans_completed ON scans(completed_at DESC)"
            )

    def save(self, result: ScanResult) -> None:
        payload = json.dumps(result.to_dict(), ensure_ascii=False)
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO scans (
                    scan_id, target, profile, started_at, completed_at,
                    duration_seconds, risk_score, grade, finding_count, payload_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    result.scan_id,
                    result.target,
                    result.profile,
                    result.started_at,
                    result.completed_at,
                    result.duration_seconds,
                    result.risk_score,
                    result.grade,
                    len(result.findings),
                    payload,
                ),
            )

    def list_summaries(self, limit: int = 250) -> list[dict[str, object]]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT scan_id, target, profile, completed_at, duration_seconds,
                       risk_score, grade, finding_count
                FROM scans ORDER BY completed_at DESC LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return [dict(row) for row in rows]

    def load(self, scan_id: str) -> ScanResult | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT payload_json FROM scans WHERE scan_id = ?", (scan_id,)
            ).fetchone()
        if not row:
            return None
        return ScanResult.from_dict(json.loads(row["payload_json"]))

    def delete(self, scan_id: str) -> None:
        with self._connect() as connection:
            connection.execute("DELETE FROM scans WHERE scan_id = ?", (scan_id,))

    def clear(self) -> None:
        with self._connect() as connection:
            connection.execute("DELETE FROM scans")
