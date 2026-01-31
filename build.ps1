# SquareScreensaver
# Copyright (c) 2026 Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

# Build requirements
# ******************
# - modern Python with tkinter
# - Windows
# - PowerShell 5+
# - PyInstaller

Remove-Item .\SquareScreensaver.zip -ErrorAction SilentlyContinue
Remove-Item .\SquareScreensaver.scr -ErrorAction SilentlyContinue
python.exe -m PyInstaller --onefile --windowed .\squarescreensaver.py --icon .\icon.ico
Move-Item .\dist\squarescreensaver.exe .
Remove-Item .\build -Recurse
Remove-Item .\dist -Recurse
Remove-Item .\squarescreensaver.spec
Move-Item .\squarescreensaver.exe .\SquareScreensaver.scr
New-Item -Path . -Name Archive -ItemType Directory
"@echo off" | Out-File .\install.cmd
"cd /d %~dp0" | Out-File .\install.cmd -Append
"powershell.exe -ExecutionPolicy Bypass -File .\installer.ps1" | Out-File .\install.cmd -Append
Copy-Item .\SquareScreensaver.scr .\Archive\
Copy-Item .\*install* .\Archive\
Copy-Item .\icon.ico .\Archive\
Copy-Item .\LICENSE .\Archive\
Remove-Item .\install.cmd
Compress-Archive -Path .\Archive\* -DestinationPath .\SquareScreensaver.zip -CompressionLevel Optimal -Verbose
Remove-Item .\Archive -Recurse