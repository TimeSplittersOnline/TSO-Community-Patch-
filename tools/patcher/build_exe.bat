@echo off
cd /d "%~dp0"
python -m pip install --upgrade pyinstaller
python tests\test_tso_data.py || (echo tso_patch.dat check failed & pause & exit /b 1)
set BG=
if exist background.png set BG=--add-data "background.png;."
python -m PyInstaller --noconfirm --clean --onefile --windowed --noupx --version-file version_info.txt --name "TSO Community Patcher" --add-data "tso_patch.dat;." %BG% "TSO Community Patcher.pyw"
echo.
echo Built "dist\TSO Community Patcher.exe"
pause
