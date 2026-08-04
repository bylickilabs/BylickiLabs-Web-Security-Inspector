from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class MetricCard(QFrame):
    def __init__(self, label: str, value: str = "—") -> None:
        super().__init__()
        self.setObjectName("MetricCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 15, 18, 15)
        layout.setSpacing(4)
        self.value_label = QLabel(value)
        self.value_label.setObjectName("MetricValue")
        self.label_label = QLabel(label)
        self.label_label.setObjectName("MetricLabel")
        self.label_label.setWordWrap(True)
        layout.addWidget(self.value_label)
        layout.addWidget(self.label_label)
        layout.addStretch(1)
        self.setMinimumHeight(105)

    def set_value(self, value: str) -> None:
        self.value_label.setText(value)

    def set_label(self, label: str) -> None:
        self.label_label.setText(label)

    def set_accent(self, color: str = "#f5f8ff") -> None:
        self.value_label.setStyleSheet(f"color: {color};")
