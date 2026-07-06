from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class Card(QFrame):
    """Reusable information card."""

    def __init__(self, title: str, value: str = "--") -> None:
        super().__init__()

        self.setObjectName("card")
        self.setMinimumSize(180, 110)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(8)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.value = QLabel(value)
        self.value.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.title.setStyleSheet("""
            color: #AAAAAA;
            font-size: 12px;
        """)

        self.value.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)

        self.setStyleSheet("""
            QFrame#card{
                background:#2b2b2b;
                border:1px solid #3c3c3c;
                border-radius:12px;
            }
        """)

    def set_value(self, text: str) -> None:
        """Update the displayed value."""
        self.value.setText(text)