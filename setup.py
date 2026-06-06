import pyautogui as pag
import time
import requests
import os
import subprocess
import sys

# Auto-install Pillow if missing
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Installing Pillow...")
    install("pillow")
    from PIL import Image, ImageDraw

# ================== CONFIG ==================
img_filename = 'Avicaidbymatrix.png'

possible_paths = [
    r"C:\Program Files (x86)\Avica\Avica.exe",
    r"C:\Program Files\Avica\Avica.exe",
    r"C:\Avica\Avica.exe",
]

actions = [
    (516, 405, 4),
    (50, 100, 1),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (447, 286, 4),
]

print("Starting Avica automation script...")

time.sleep(8)

def find_avica_exe():
    for path in possible_paths:
        if os.path.exists(path):
            print(f"Found Avica at: {path}")
            return path
    print("Deep searching for Avica.exe...")
    try:
        for root, dirs, files in os.walk("C:\\"):
            if "Avica.exe" in files:
                full_path = os.path.join(root, "Avica.exe")
                print(f"Found via search: {full_path}")
                return full_path
    except:
        pass
    return None

def upload_image_to_gofile(img_filename):
    url = 'https://store1.gofile.io/uploadFile'
    try:
        with open(img_filename, 'rb') as img_file:
            files = {'file': img_file}
            response = requests.post(url, files=files, timeout=30)
            response.raise_for_status()
            result = response.json()

            if result.get('status') == 'ok':
                download_page = result['data']['downloadPage']
                with open('show.bat', 'a', encoding='utf-8') as bat_file:
                    bat_file.write(f'\necho Avica Remote ID : {download_page}')
                print(f"Upload successful -> {download_page}")
                return download_page
            else:
                print("Upload error:", result.get('status'))
                return None
    except Exception as e:
        print(f"Upload failed: {e}")
        return None

# === Find & Launch Avica ===
avica_path = find_avica_exe()

if not avica_path:
    print("Avica.exe not found on this runner.")
else:
    try:
        print(f"Launching: {avica_path}")
        subprocess.Popen([avica_path])
        time.sleep(10)
    except Exception as e:
        print(f"Launch failed: {e}")

# === Main Click Sequence ===
for i, (x, y, duration) in enumerate(actions, 1):
    try:
        pag.click(x, y, duration=duration)
        print(f"Step {i}: Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Click failed at ({x}, {y}): {e}")

    if (x, y) == (249, 203):
        time.sleep(2)
        try:
            pag.click(x, y, duration=duration)
        except:
            pass

    if (x, y) == (447, 286):
        time.sleep(12)

        # Screenshot with fallback
        try:
            print("Taking screenshot...")
            screenshot = pag.screenshot()
            screenshot.save(img_filename)
            print("Screenshot saved successfully")
        except Exception as e:
            print(f"Screenshot failed (normal in headless): {e}")
            try:
                img = Image.new('RGB', (1024, 768), color=(10, 10, 30))
                draw = ImageDraw.Draw(img)
                draw.text((80, 80), "Avica Automation\nScreenshot failed - Headless Runner", fill=(255, 255, 100))
                img.save(img_filename)
                print("Dummy screenshot created")
            except:
                open(img_filename, 'w').close()

        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print("Image uploaded successfully!")
        else:
            print("Upload failed")

    time.sleep(8)

print("Script finished!")
