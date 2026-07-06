from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Sidebar(QWidget):
    """Application navigation sidebar."""

    page_selected = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(220)

        self.list = QListWidget()

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
            QListWidgetItem(page, self.list)

        self.list.setCurrentRow(0)
        self.list.currentRowChanged.connect(self.page_selected.emit)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.addWidget(self.list)