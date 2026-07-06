from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from acc.ui.widgets.card import Card


class DashboardPage(QWidget):
    """Main dashboard page."""

    def __init__(self) -> None:
        super().__init__()

        root = QVBoxLayout(self)
        root.setContentsMargins(30, 30, 30, 30)
        root.setSpacing(20)

        title = QLabel("Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Overview of your connected Android device."
        )

        subtitle.setStyleSheet("""
            color:#aaaaaa;
            font-size:14px;
        """)

        root.addWidget(title)
        root.addWidget(subtitle)

        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        self.device_card = Card(
            "Device",
            "Not Connected",
            "📱",
            "Waiting for USB..."
        )

        self.battery_card = Card(
            "Battery",
            "-- %",
            "🔋",
            "Unknown"
        )

        self.storage_card = Card(
            "Storage", 
            "-- GB",
            "💾",
            "Unknown"
        )

        self.android_card = Card(
             "Android",
             "--",
             "🤖",
             "Version"
        )     

        grid.addWidget(self.device_card, 0, 0)
        grid.addWidget(self.battery_card, 0, 1)
        grid.addWidget(self.storage_card, 0, 2)
        grid.addWidget(self.android_card, 0, 3)
        recent_title = QLabel("Recent Activity")
        recent_title.setObjectName("sectionTitle")

        recent_activity = Card(
            "Activity",
            "No Activity",
            "📋",
            "Waiting for your first device..."
        )

        root.addSpacing(20)
        root.addWidget(recent_title)
        root.addWidget(recent_activity)

        root.addLayout(grid)
        root.addStretch()