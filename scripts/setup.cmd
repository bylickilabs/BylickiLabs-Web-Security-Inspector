@echo off
setlocal
cd /d "%~dp0\.."
where py >nul 2>nul
if %errorlevel%==0 (
  set PYTHON=py -3
) else (
  set PYTHON=python
)
%PYTHON% -m venv .venv
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 goto :error
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto :error
echo.
echo Installation completed successfully.
echo Start the application with scripts\run.cmd
pause
exit /b 0
:error
echo.
echo Installation failed. Review the messages above.
pause
exit /b 1
