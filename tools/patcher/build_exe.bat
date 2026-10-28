@echo off
cd /d "%~dp0"
python -m pip install --upgrade pyinstaller
python tests\test_tso_data.py || (echo tso_patch.dat check failed & pause & exit /b 1)
python -m PyInstaller --onefile --windowed --name "TSO Community Patcher" --add-data "tso_patch.dat;." "TSO Community Patcher.pyw"
echo.
echo Built "dist\TSO Community Patcher.exe"
pause
