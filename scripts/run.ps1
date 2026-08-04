$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
if (-not (Test-Path .\.venv\Scripts\python.exe)) { throw "Run setup.ps1 first." }
& .\.venv\Scripts\python.exe main.py
