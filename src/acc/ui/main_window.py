from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from acc.ui.pages.dashboard_page import DashboardPage
from acc.ui.pages.devices_page import DevicesPage
from acc.ui.widgets.header import Header
from acc.ui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Android Control Center")
        self.resize(1400, 850)

        # ---------- Sidebar ----------
        self.sidebar = Sidebar()

        # ---------- Pages ----------
        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.devices_page = DevicesPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.devices_page)

        # Placeholder pages
        for _ in range(6):
            placeholder = QWidget()
            self.pages.addWidget(placeholder)

        # ---------- Connect Sidebar ----------
        self.sidebar.page_changed.connect(self.change_page)

        # ---------- Widgets ----------
        self.header = Header()

        central = QWidget()
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        content_layout.addWidget(self.header)
        content_layout.addWidget(self.pages)

        main_layout.addWidget(self.sidebar)
        main_layout.addLayout(content_layout)

        self.setCentralWidget(central)

        # ---------- Status Bar ----------
        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def change_page(self, page: int) -> None:
        """Switch visible page."""

        if 0 <= page < self.pages.count():
            self.pages.setCurrentIndex(page)