from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Android Control Center")
        self.resize(1400, 850)

        self._create_toolbar()
        self._create_statusbar()
        self._create_ui()

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

    def _create_statusbar(self) -> None:
        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def _create_ui(self) -> None:
        central = QWidget()

        layout = QVBoxLayout(central)

        label = QLabel("Android Control Center")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        self.setCentralWidget(central)