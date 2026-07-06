from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QStatusBar,
    QWidget,
)

from acc.ui.pages.dashboard_page import DashboardPage
from acc.ui.pages.devices_page import DevicesPage
from acc.ui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Android Control Center")
        self.resize(1450, 900)

        self.sidebar = Sidebar()

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()
        self.devices = DevicesPage()

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.devices)

        self.sidebar.page_changed.connect(self.stack.setCurrentIndex)

        central = QWidget()

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.setCentralWidget(central)

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)