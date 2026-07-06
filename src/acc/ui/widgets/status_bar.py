from __future__ import annotations

from enum import Enum

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Page(Enum):
    HOME = "Home"
    DEVICES = "Devices"
    FILES = "Files"
    APPS = "Apps"
    SCREEN = "Screen"
    TERMINAL = "Terminal"
    SETTINGS = "Settings"


class Sidebar(QWidget):
    """
    Left navigation sidebar.
    """

    page_changed = Signal(Page)

    def __init__(self) -> None:
        super().__init__()

        self.setMinimumWidth(220)
        self.setMaximumWidth(220)

        self._list = QListWidget()
        self._list.setSpacing(4)
        self._list.currentRowChanged.connect(self._row_changed)

        for page in Page:
            QListWidgetItem(page.value, self._list)

        self._list.setCurrentRow(0)

        layout = QVBoxLayout(self)
        layout.addWidget(self._list)

        self.setLayout(layout)

        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Expanding,
        )

    def _row_changed(self, row: int) -> None:
        if row < 0:
            return

        self.page_changed.emit(list(Page)[row])