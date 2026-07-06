from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DashboardPage(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Welcome to Android Control Center.\n\n"
            "Connect an Android device to begin."
        )

        subtitle.setStyleSheet("""
            font-size:15px;
            color:#bbbbbb;
        """)

        layout.addWidget(title)
        layout.addSpacing(15)
        layout.addWidget(subtitle)
        layout.addStretch()