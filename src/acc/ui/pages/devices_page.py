from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DevicesPage(QWidget):
    """Devices page."""

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Devices")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setStyleSheet(
            """
            font-size: 28px;
            font-weight: bold;
            """
        )

        info = QLabel(
            "No Android device connected."
        )

        info.setStyleSheet(
            "font-size:14px; color:#bdbdbd;"
        )

        layout.addWidget(title)
        layout.addSpacing(15)
        layout.addWidget(info)
        layout.addStretch()