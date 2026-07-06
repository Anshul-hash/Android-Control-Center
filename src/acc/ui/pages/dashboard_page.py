from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DashboardPage(QWidget):
    """Dashboard page."""

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet(
            """
            font-size: 28px;
            font-weight: bold;
            """
        )

        subtitle = QLabel(
            "Welcome to Android Control Center.\n\n"
            "Connect an Android device to get started."
        )
        subtitle.setStyleSheet("font-size: 14px; color: #bdbdbd;")

        layout.addWidget(title)
        layout.addSpacing(15)
        layout.addWidget(subtitle)
        layout.addStretch()