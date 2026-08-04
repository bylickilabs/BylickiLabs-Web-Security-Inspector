@echo off
setlocal
cd /d "%~dp0\.."
if not exist ".venv\Scripts\pyinstaller.exe" (
  echo PyInstaller not found. Run scripts\setup_dev.cmd first.
  pause
  exit /b 1
)
.venv\Scripts\pyinstaller.exe --noconfirm --clean BylickiLabsWebSecurityInspector.spec
if errorlevel 1 pause