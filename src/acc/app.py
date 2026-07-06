from __future__ import annotations

import logging
import sys

from PySide6.QtWidgets import QApplication

from acc.ui.main_window import MainWindow
from acc.ui.theme import apply_theme 


def configure_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def run() -> None:
    """Application entry point."""

    configure_logging()

    app = QApplication(sys.argv)

    apply_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())