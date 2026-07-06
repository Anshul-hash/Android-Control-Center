from __future__ import annotations

from PySide6.QtCore import Qt, Signal, QSize 
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton


class NavigationButton(QPushButton):
    """Sidebar navigation button."""

    clicked_page = Signal(int)

    def __init__(
        self,
        text: str,
        icon: QIcon,
        page_index: int,
    ) -> None:
        super().__init__(text)

        self.page_index = page_index

        self.setIcon(icon)
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(52)
        self.setIconSize(QSize(20, 20))
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.setStyleSheet("""
             text-align:left;
             padding-left:14px;
         """)

        self.clicked.connect(self._emit_page)

    def _emit_page(self) -> None:
        self.clicked_page.emit(self.page_index)