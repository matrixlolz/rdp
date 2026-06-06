import pyautogui as pag
import time
import requests
import os
import subprocess
import sys
from PIL import Image, ImageDraw  # For dummy screenshot fallback

# ================== CONFIG ==================
img_filename = 'Avicaidbymatrix.png'

# Possible locations for Avica
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

print("🚀 Starting Avica automation script...")

time.sleep(8)

def find_avica_exe():
    """Search for Avica.exe"""
    for path in possible_paths:
        if os.path.exists(path):
            print(f"✅ Found Avica at: {path}")
            return path
    
    # Deep search
    print("🔍 Searching for Avica.exe...")
    try:
        for root, dirs, files in os.walk("C:\\"):
            if "Avica.exe" in files:
                full_path = os.path.join(root, "Avica.exe")
                print(f"✅ Found via search: {full_path}")
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
                print(f"✅ Upload successful → {download_page}")
                return download_page
            else:
                print("Upload error:", result.get('status'))
                return None
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return None

# === Find & Launch Avica ===
avica_path = find_avica_exe()

if not avica_path:
    print("❌ Could not find Avica.exe!")
    print("Please make sure Avica is installed.")
    print("Download: https://www.avica.com/downloads/")
    sys.exit(1)

try:
    print(f"Launching Avica: {avica_path}")
    subprocess.Popen([avica_path])
    time.sleep(10)   # Wait for window to appear
except Exception as e:
    print(f"Failed to launch Avica: {e}")
    sys.exit(1)

# === Main Click Sequence ===
for i, (x, y, duration) in enumerate(actions, 1):
    try:
        pag.click(x, y, duration=duration)
        print(f"Step {i}: Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Click failed at ({x}, {y}): {e}")

    if (x, y) == (249, 203):   # Allow Remote Access button
        time.sleep(2)
        pag.click(x, y, duration=duration)

    if (x, y) == (447, 286):   # Final step - Screenshot + Upload
        time.sleep(12)

        # Take Screenshot with fallback
        try:
            print("📸 Taking screenshot...")
            screenshot = pag.screenshot()
            screenshot.save(img_filename)
            print("✅ Screenshot saved")
        except Exception as e:
            print(f"⚠️ Screenshot failed: {e}")
            # Create dummy image
            try:
                img = Image.new('RGB', (1024, 768), color=(20, 20, 40))
                draw = ImageDraw.Draw(img)
                draw.text((100, 100), "Screenshot failed\n(Headless environment?)", fill=(255, 255, 255))
                img.save(img_filename)
                print("✅ Dummy image created")
            except:
                open(img_filename, 'w').close()

        # Upload
        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print("🎉 Image uploaded successfully!")
        else:
            print("❌ Upload failed")

    time.sleep(8)

print("✅ Script completed!")
