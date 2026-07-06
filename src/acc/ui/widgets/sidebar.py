from __future__ import annotations

from enum import IntEnum

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QLabel, 
    QVBoxLayout,
    QWidget,
)

from acc.resources.icons import icon
from acc.ui.widgets.navigation_button import NavigationButton


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
    """Application sidebar."""

    page_changed = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(230)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)
        title = QLabel("Android Control Center")
        title.setObjectName("sidebarTitle")

        layout.addWidget(title)
        layout.addSpacing(16)


        self.buttons = []

        pages = [
            ("dashboard", "Dashboard"),
            ("devices", "Devices"),
            ("files", "Files"),
            ("apps", "Apps"),
            ("screen", "Screen"),
            ("camera", "Camera"),
            ("terminal", "Terminal"),
        ]

        for index, (icon_name, title) in enumerate(pages):

            button = NavigationButton(
                title,
                icon(icon_name),
                index,
            )

            button.clicked_page.connect(self.change_page)

            self.buttons.append(button)

            layout.addWidget(button)

        layout.addStretch()

        settings = NavigationButton(
            "Settings",
            icon("settings"),
            Page.SETTINGS,
        )

        settings.clicked_page.connect(self.change_page)

        self.buttons.append(settings)

        layout.addWidget(settings)

        self.buttons[0].setChecked(True)

    def change_page(self, index: int) -> None:

        for button in self.buttons:
            button.setChecked(False)

        self.buttons[index].setChecked(True)

        self.page_changed.emit(index)