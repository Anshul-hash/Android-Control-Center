from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QStackedWidget,
)

from acc.ui.pages.home_page import HomePage
from acc.ui.pages.devices_page import DevicesPage
from acc.ui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Android Control Center")
        self.resize(1400, 850)

        self.sidebar = Sidebar()

        self.stack = QStackedWidget()

        self.home = HomePage()
        self.devices = DevicesPage()

        self.stack.addWidget(self.home)
        self.stack.addWidget(self.devices)

        self.sidebar.page_selected.connect(self.change_page)

        central = QWidget()

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.setCentralWidget(central)

        self.statusBar().showMessage("Ready")

    def change_page(self, index: int) -> None:
        if index < self.stack.count():
            self.stack.setCurrentIndex(index)