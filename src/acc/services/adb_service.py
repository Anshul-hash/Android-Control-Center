from __future__ import annotations

import subprocess
from typing import List


class ADBService:
    """Provides high-level access to Android Debug Bridge."""

    def __init__(self, adb_path: str = "adb") -> None:
        self._adb_path = adb_path

    def _run(self, *args: str) -> subprocess.CompletedProcess[str]:
        """
        Execute an adb command.

        Example:
            self._run("devices")
            self._run("shell", "getprop")
        """
        return subprocess.run(
            [self._adb_path, *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def version(self) -> str:
        """Return the installed ADB version."""
        return self._run("version").stdout.strip()

    def list_devices(self) -> List[str]:
        """
        Return connected device serial numbers.
        """
        output = self._run("devices").stdout

        devices: List[str] = []

        for line in output.splitlines()[1:]:

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) >= 2 and parts[1] == "device":
                devices.append(parts[0])

        return devices

    def has_devices(self) -> bool:
        """Return True if at least one device is connected."""
        return bool(self.list_devices())