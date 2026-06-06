import pyautogui as pag
import time
import requests
import os
import subprocess
import sys

# --- Configuration ---
img_filename = 'Avicaidbymatrix.png'

# Possible Avica paths - we'll try them in order
possible_avica_paths = [
    r"C:\Program Files (x86)\Avica\Avica.exe",
    r"C:\Program Files\Avica\Avica.exe",
    r"C:\Avica\Avica.exe",
    # Add more if you know custom location
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

print("Starting Avica automation...")

time.sleep(5)

def find_avica_exe():
    """Try to locate Avica.exe"""
    for path in possible_avica_paths:
        if os.path.exists(path):
            print(f"✅ Found Avica at: {path}")
            return path
    # Fallback: search in common locations
    try:
        import glob
        for drive in ['C:']:
            for p in glob.glob(f"{drive}\\**\\Avica.exe", recursive=True):
                if "Avica" in p:
                    print(f"✅ Found Avica via search: {p}")
                    return p
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
                print(f"✅ Upload successful: {download_page}")
                return download_page
            else:
                print("Upload error:", result.get('status'))
                return None
    except Exception as e:
        print(f"Failed to upload image: {e}")
        return None

# === Find and Launch Avica ===
avica_path = find_avica_exe()

if not avica_path:
    print("❌ Avica.exe not found! Please install Avica first.")
    print("Download it from: https://www.avica.com/downloads/")
    sys.exit(1)

try:
    print(f"Launching: {avica_path}")
    subprocess.Popen([avica_path])
    time.sleep(10)  # Wait longer for GUI to load
except Exception as e:
    print(f"Failed to launch Avica: {e}")
    sys.exit(1)

# === Click Sequence ===
for idx, (x, y, duration) in enumerate(actions):
    try:
        pag.click(x, y, duration=duration)
        print(f"Clicked {idx+1}/{len(actions)} at ({x}, {y})")
    except Exception as e:
        print(f"Click failed at ({x}, {y}): {e}")

    if (x, y) == (249, 203):
        time.sleep(2)
        pag.click(x, y, duration=duration)  # Double click for "Allow"

    if (x, y) == (447, 286):
        time.sleep(12)

        # Take screenshot with fallback
        try:
            print("Taking screenshot...")
            screenshot = pag.screenshot()
            screenshot.save(img_filename)
            print(f"Screenshot saved: {img_filename}")
        except Exception as e:
            print(f"Screenshot failed: {e}")
            # Create dummy image
            try:
                from PIL import Image, ImageDraw, ImageFont
                img = Image.new('RGB', (1024, 768), color=(0, 0, 0))
                draw = ImageDraw.Draw(img)
                draw.text((100, 100), "Screenshot failed\nRunning in headless mode?", fill=(255, 255, 255))
                img.save(img_filename)
                print("Dummy image created")
            except:
                open(img_filename, 'a').close()  # Empty file as last resort

        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print(f"✅ Image uploaded successfully!")
        else:
            print("❌ Upload failed")

    time.sleep(8)

print('✅ Script finished!')
