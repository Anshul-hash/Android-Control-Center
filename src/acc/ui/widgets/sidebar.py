from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QWidget


class Sidebar(QWidget):

    page_changed = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(220)

        self.menu = QListWidget()

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

        self.menu.currentRowChanged.connect(self.page_changed)

        self.menu.setCurrentRow(0)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.menu)