# SquareScreensaver
# Copyright (c) 2026 Karl "karl152"
# This software is licensed under the BSD 3-Clause License.
# See the LICENSE file for details.
# SPDX-License-Identifier: BSD-3-Clause

try{Remove-Item C:\Windows\System32\SquareScreensaver.scr}catch{exit}
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\SquareScreensaver" -Recurse -Force
Remove-Item -Path 'C:\Program Files\SquareScreensaver' -Recurse -Force
$DeleteCommand = "Write-Host 'Finishing uninstallation...'; Start-Sleep 2; Remove-Item 'C:\Program Files\SquareScreensaver' -Recurse -Force"
Start-Process powershell.exe -ArgumentList "-NoProfile -Command $DeleteCommand"