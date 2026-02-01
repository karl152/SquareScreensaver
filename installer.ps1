# SquareScreensaver
# Copyright (c) 2026 Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

Write-Host 'SquareScreensaver
Copyright (c) 2026 Karl "karl152"
This software is licensed under the BSD 3-Clause License.
See the LICENSE file for details.
SPDX-License-Identifier: BSD-3-Clause
'

# look for existing installation
if (Test-Path 'C:\Program Files\SquareScreensaver' -PathType Container) {
    Read-Host "SquareScreensaver seems to be already installed. Press enter to exit"
    exit
}
# try to install the screensaver
try {Copy-Item .\SquareScreensaver.scr C:\Windows\System32\ -ErrorAction Stop}
catch {
Read-Host "You must extract the ZIP file and run the installer as Administrator. Press enter to exit."
exit 1
}

# create directory in program files with uninstaller
New-Item -Path 'C:\Program Files' -Name SquareScreensaver -ItemType Directory -Force
Copy-Item .\uninstaller.ps1 'C:\Program Files\SquareScreensaver\'
Copy-Item .\icon.ico 'C:\Program Files\SquareScreensaver\'
Copy-Item .\LICENSE 'C:\Program Files\SquareScreensaver\'
"@echo off" | Out-File 'C:\Program Files\SquareScreensaver\uninstall.cmd' -Encoding ascii
'powershell.exe -ExecutionPolicy Bypass -File "C:\Program Files\SquareScreensaver\uninstaller.ps1"' | Out-File 'C:\Program Files\SquareScreensaver\uninstall.cmd' -Encoding ascii -Append

# register program
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver"
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "DisplayName" -PropertyType String -Value "SquareScreensaver" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "DisplayVersion" -PropertyType String -Value "1.0" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "UninstallString" -PropertyType String -Value "C:\Program Files\SquareScreensaver\uninstall.cmd" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "Publisher" -PropertyType String -Value "karl152" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "InstallLocation" -PropertyType String -Value "C:\Program Files\SquareScreensaver" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "DisplayIcon" -PropertyType String -Value "C:\Program Files\SquareScreensaver\icon.ico" -Force
Write-Host
Read-Host -Prompt "Press enter to exit"
