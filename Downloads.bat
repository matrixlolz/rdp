@echo off
curl -s -L -o setup.py https://github.com/voidxmatrix/rdp/blob/main/setup.py
curl -s -L -o AvicaLite_v8.0.8.9.exe "https://download.avica.com/AvicaLite_v8.0.8.9.exe?_gl=1*2w6u98*_gcl_au*MTEwNDQ3OTIwNC4xNzI5Mzg2MzIz"
curl -s -L -o show.bat https://github.com/voidxmatrix/rdp/blob/main/show.bat
curl -s -L -o loop.bat https://github.com/voidxmatrix/rdp/blob/main/loop.bat
curl -s -L -o C:\Users\Public\Desktop\Telegram.exe https://telegram.org/dl/desktop/win64
curl -s -L -o C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-621.exe
curl -s -L -o wall.bat https://github.com/voidxmatrix/rdp/blob/main/wall.bat
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
python.exe -m pip install --upgrade pip
pip install requests --quiet
pip install pyautogui --quiet
pip install telegraph --quiet

C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
net user runneradmin TheDisa1a
python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"
start "" "AvicaLite_v8.0.8.9.exe"
python setup.py
call wall.bat
