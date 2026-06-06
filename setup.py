import pyautogui as pag
import time
import requests
import os
import subprocess
import sys

# Auto-install Pillow
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Installing Pillow...")
    install("pillow")
    from PIL import Image, ImageDraw

print("Starting AvicaLite automation...")

time.sleep(12)

# Launch AvicaLite
try:
    subprocess.Popen(["AvicaLite_v8.0.8.9.exe"])
    print("Launched AvicaLite")
except:
    print("AvicaLite already running")

time.sleep(18)

# Optimized click sequence
actions = [
    (960, 540, 3),   # Focus
    (900, 650, 3),
    (516, 405, 3),
    (50, 100, 2),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (447, 286, 4),
]

for i, (x, y, duration) in enumerate(actions, 1):
    try:
        pag.click(x, y, duration=duration)
        print(f"Step {i}: Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Click failed: {e}")
    time.sleep(4)

# Extra clicks for Allow button
time.sleep(6)
pag.click(249, 203, duration=3)
time.sleep(6)
pag.click(249, 203, duration=3)

time.sleep(15)

# Screenshot
try:
    print("Taking screenshot...")
    screenshot = pag.screenshot()
    screenshot.save('Avicaidbymatrix.png')
    print("Screenshot saved")
except Exception as e:
    print(f"Screenshot failed: {e}")
    img = Image.new('RGB', (1280, 720), color=(0, 0, 40))
    draw = ImageDraw.Draw(img)
    draw.text((100, 100), "Avica Remote ID\nCheck show.bat", fill=(0, 255, 255))
    img.save('Avicaidbymatrix.png')

# Upload + Create clean show.bat
def upload_to_gofile():
    try:
        with open('Avicaidbymatrix.png', 'rb') as f:
            response = requests.post('https://store1.gofile.io/uploadFile', files={'file': f}, timeout=30)
            result = response.json()
            if result.get('status') == 'ok':
                link = result['data']['downloadPage']
                
                with open('show.bat', 'w', encoding='utf-8') as bat:
                    bat.write('@echo off\n')
                    bat.write('echo.\n')
                    bat.write('echo ================================================\n')
                    bat.write('echo          Avica Remote Access Info\n')
                    bat.write('echo ================================================\n')
                    bat.write('echo.\n')
                    bat.write('echo Telegram: https://t.me/ishowmatrix\n')
                    bat.write('echo.\n')
                    bat.write('echo Created by a Indian Matrix\n')
                    bat.write('echo ************************\n')
                    bat.write('echo Corrected Once Again Thanks to the People Who Reported It\n')
                    bat.write('echo ************************\n')
                    bat.write('echo *And That Matrix Doesn\'t Take Defiance Home.*\n')
                    bat.write('echo ************************\n')
                    bat.write('echo #Teamvoid\n')
                    bat.write('echo.\n')
                    bat.write('echo User name : runneradmin\n')
                    bat.write('echo User Pass : TheMatr1x\n')
                    bat.write('echo.\n')
                    bat.write('echo Avica Remote ID Link:\n')
                    bat.write(f'echo {link}\n')
                    bat.write('echo.\n')
                    bat.write('echo Click the link above to see ID and Password\n')
                    bat.write('echo.\n')
                    bat.write('pause\n')
                print(f"Avica Remote ID: {link}")
                return link
    except Exception as e:
        print(f"Upload failed: {e}")
    return None

upload_to_gofile()

print("Avica setup finished successfully!")
