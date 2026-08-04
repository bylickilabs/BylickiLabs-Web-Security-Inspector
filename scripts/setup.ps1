$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
$python = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { "python" }
if ($python -eq "py") { & py -3 -m venv .venv } else { & python -m venv .venv }
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
Write-Host "Installation completed. Start with .\scripts\run.ps1"
