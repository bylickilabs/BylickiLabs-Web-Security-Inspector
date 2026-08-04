@echo off
setlocal
cd /d "%~dp0\.."
if not exist ".venv\Scripts\python.exe" (
  echo Run scripts\setup_dev.cmd first.
  pause
  exit /b 1
)
.venv\Scripts\python.exe -m compileall -q app main.py tests
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m ruff check app tests main.py
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m pytest
if errorlevel 1 goto :error
echo Quality checks completed successfully.
exit /b 0
:error
echo Quality checks failed.
pause
exit /b 1
