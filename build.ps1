# SquareScreensaver
# Copyright (c) 2026 Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

# Build requirements
# ******************
# - modern Python with tkinter
# - Windows
# - PowerShell
# - PyInstaller

Remove-Item .\SquareScreensaver.scr -ErrorAction SilentlyContinue
python.exe -m PyInstaller --onefile --windowed .\squarescreensaver.py --icon .\icon.ico
Move-Item .\dist\squarescreensaver.exe .
Remove-Item .\build -Recurse
Remove-Item .\dist -Recurse
Remove-Item .\squarescreensaver.spec
Move-Item .\squarescreensaver.exe .\SquareScreensaver.scr