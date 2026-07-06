from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
)


class Header(QFrame):
    """Application header."""

    def __init__(self) -> None:
        super().__init__()

        self.setFixedHeight(60)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)

        title = QLabel("🤖 Android Control Center")

        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        self.device_status = QLabel("🔴 No Device Connected")

        self.refresh_button = QPushButton("Refresh")

        layout.addWidget(title)

        layout.addStretch()

        layout.addWidget(self.device_status)

        layout.addSpacing(20)

        layout.addWidget(self.refresh_button)