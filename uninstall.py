# SquareScreensaver
# Copyright (c) 2026 Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

import subprocess
from pathlib import Path

print("checking PowerShell version...")
if Path(r"C:\Program Files\PowerShell\7\pwsh.exe").exists():
    print("starting uninstaller with PowerShell 7")
    subprocess.Popen([r"C:\Program Files\PowerShell\7\pwsh.exe", "-ExecutionPolicy", "Bypass", r"C:\Program Files\SquareScreensaver\uninstaller.ps1"])
else:
    print("starting Uninstaller with Windows PowerShell")
    subprocess.Popen(["powershell", "-ExecutionPolicy", "Bypass", r"C:\Program Files\SquareScreensaver\uninstaller.ps1"])
