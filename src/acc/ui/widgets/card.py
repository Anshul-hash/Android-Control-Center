from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class Card(QFrame):
    """Reusable information card."""

    def __init__(
        self,
        title: str,
        value: str = "--",
        icon: str = "📄",
        subtitle: str = "",
    ) -> None:
    
        super().__init__()

        self.setObjectName("card")
        from PySide6.QtWidgets import QSizePolicy

        self.setMinimumHeight(150)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )    

        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(8)

        self.icon = QLabel(icon)
        self.icon.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.value = QLabel(value)
        self.value.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.subtitle = QLabel(subtitle)
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.icon.setObjectName("cardIcon")
        self.title.setObjectName("cardTitle")
        self.value.setObjectName("cardValue")
        self.subtitle.setObjectName("cardSubtitle")

        layout.addWidget(self.icon)
        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)
        layout.addWidget(self.subtitle)

    def set_value(self, text: str) -> None:
        """Update the displayed value."""
        self.value.setText(text)