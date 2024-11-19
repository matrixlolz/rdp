@echo off
powershell -Command "Invoke-WebRequest https://gitlab.com/rdp7214147/rdp-avica/-/raw/main/matrix.jpg -OutFile TranscodedWallpaper"

powershell -Command "Invoke-WebRequest https://gitlab.com/rdp7214147/rdp-avica/-/blob/main/matrix.jpg -OutFile matrix.jpg"

set "TranscodedWallpaper=TranscodedWallpaper"
set "matrix.jpg"

set "destinationDir=C:\Users\runneradmin\AppData\Roaming\Microsoft\Windows\Themes"
set "cachedFileDir=C:\Users\runneradmin\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles"

copy /y "%TranscodedWallpaper%" "%destinationDir%\TranscodedWallpaper"
copy /y "%CachedImage%" "%cachedFileDir%\matrix.jpg"

RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True