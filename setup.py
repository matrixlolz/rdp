import pyautogui as pag
import time
import requests
import os
import subprocess
import sys

# Auto install Pillow
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Installing Pillow...")
    install("pillow")
    from PIL import Image, ImageDraw

img_filename = 'Avicaidbymatrix.png'

print("Starting Avica automation...")

time.sleep(10)

# Launch Avica (already started in Downloads.bat, but ensure it's running)
try:
    subprocess.Popen([r"AvicaLite_v8.0.8.9.exe"])
    print("Launched AvicaLite")
except:
    print("Avica already running or launch failed")

time.sleep(15)  # Important: Wait for Avica window to fully load

# Improved click sequence for Avica setup
actions = [
    (900, 600, 3),   # Main window / Get Started
    (516, 405, 3),
    (50, 100, 2),
    (249, 203, 4),   # Allow remote access (multiple clicks)
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (447, 286, 4),   # Final step
]

for i, (x, y, duration) in enumerate(actions, 1):
    try:
        pag.click(x, y, duration=duration)
        print(f"Step {i}: Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Click failed: {e}")

    if (x, y) in [(249, 203), (447, 286)]:
        time.sleep(3)
        pag.click(x, y, duration=2)  # Extra click for confirmation

    time.sleep(6)

# Take screenshot of Avica ID
time.sleep(12)
try:
    print("Taking screenshot of Avica ID...")
    screenshot = pag.screenshot()
    screenshot.save(img_filename)
    print("Screenshot saved")
except Exception as e:
    print(f"Screenshot failed: {e}")
    # Dummy image
    img = Image.new('RGB', (1280, 720), color=(0, 0, 40))
    draw = ImageDraw.Draw(img)
    draw.text((100, 100), "Avica Remote ID Screenshot\n(Headless Mode)", fill=(0, 255, 255))
    img.save(img_filename)

# Upload
def upload_to_gofile(img_filename):
    try:
        with open(img_filename, 'rb') as f:
            response = requests.post('https://store1.gofile.io/uploadFile', files={'file': f}, timeout=30)
            result = response.json()
            if result.get('status') == 'ok':
                link = result['data']['downloadPage']
                with open('show.bat', 'a', encoding='utf-8') as bat:
                    bat.write(f'\necho Avica Remote ID Link: {link}')
                print(f"Avica ID uploaded: {link}")
                return link
    except Exception as e:
        print(f"Upload error: {e}")
    return None

upload_to_gofile(img_filename)

print("Avica setup completed!")
