from __future__ import annotations

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QStatusBar,
)

from acc.ui.pages.dashboard_page import DashboardPage
from acc.ui.pages.devices_page import DevicesPage


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Android Control Center")
        self.resize(1400, 850)

        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.devices_page = DevicesPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.devices_page)

        self.setCentralWidget(self.pages)

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)