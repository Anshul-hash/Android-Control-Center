from __future__ import annotations

from enum import IntEnum

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Page(IntEnum):
    DASHBOARD = 0
    DEVICES = 1
    FILES = 2
    APPS = 3
    SCREEN = 4
    CAMERA = 5
    TERMINAL = 6
    SETTINGS = 7


class Sidebar(QWidget):
    """
    Left navigation panel.
    """

    page_changed = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(230)

        self.menu = QListWidget()
        self.menu.setSpacing(4)
        self.menu.setAlternatingRowColors(False)

        pages = [
            "🏠 Dashboard",
            "📱 Devices",
            "📂 Files",
            "📦 Apps",
            "🖥 Screen",
            "📷 Camera",
            "💻 Terminal",
            "⚙ Settings",
        ]

        for page in pages:
            QListWidgetItem(page, self.menu)

        self.menu.setCurrentRow(Page.DASHBOARD)

        self.menu.currentRowChanged.connect(
            self.page_changed.emit
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.addWidget(self.menu)