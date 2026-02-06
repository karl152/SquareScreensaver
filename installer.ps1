# SquareScreensaver
# Copyright (c) 2026 Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

Write-Host
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
# check Windows version
if ([System.Environment]::OSVersion.Version.Major -ne 10) {
    Read-Host "This software is compatible with Windows NT 10 only. Press enter to exit."
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
Copy-Item .\uninstall.exe 'C:\Program Files\SquareScreensaver\'
Copy-Item .\LICENSE 'C:\Program Files\SquareScreensaver\'

# register program
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver"
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "DisplayName" -PropertyType String -Value "SquareScreensaver" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "DisplayVersion" -PropertyType String -Value "1.2" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "UninstallString" -PropertyType String -Value "C:\Program Files\SquareScreensaver\uninstall.exe" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "Publisher" -PropertyType String -Value "karl152" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "InstallLocation" -PropertyType String -Value "C:\Program Files\SquareScreensaver" -Force
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Name "DisplayIcon" -PropertyType String -Value "C:\Program Files\SquareScreensaver\uninstall.exe" -Force
Write-Host
Read-Host -Prompt "Done! Press enter to exit"