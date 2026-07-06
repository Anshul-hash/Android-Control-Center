from __future__ import annotations

from pathlib import Path

from PySide6.QtGui import QIcon


# Project root (Android-Control-Center/)
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# assets/icons/
ICON_DIR = PROJECT_ROOT / "assets" / "icons"


def icon(name: str) -> QIcon:
    """
    Load an SVG icon from assets/icons.

    Example:
        button.setIcon(icon("refresh"))
    """
    return QIcon(str(ICON_DIR / f"{name}.svg"))