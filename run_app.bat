@echo off
:: Get the current directory of the batch file
set "currentDir=%~dp0"
echo Current Directory: %currentDir%

:: Change to the current directory
cd /d "%currentDir%"

:: Get the path to the Python executable (assuming Python is in your PATH)
for /f "delims=" %%i in ('where pythonw') do set pythonPath=%%i

:: Run the Python script using pythonw.exe (this hides the console window)
pythonw "%pythonPath%" pythonapp.py

pause