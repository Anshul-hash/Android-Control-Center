from __future__ import annotations

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QStatusBar,
)

from acc.ui.pages.home_page import HomePage
from acc.ui.pages.devices_page import DevicesPage


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Android Control Center")
        self.resize(1400, 850)

        self._stack = QStackedWidget()

        self.home_page = HomePage()
        self.devices_page = DevicesPage()

        self._stack.addWidget(self.home_page)
        self._stack.addWidget(self.devices_page)

        self.setCentralWidget(self._stack)

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)