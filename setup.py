import pyautogui as pag
import time
import requests
import os
import subprocess
import sys

# --- Configuration ---
img_filename = 'Avicaidbymatrix.png'
avica_path = r"C:\Program Files (x86)\Avica\Avica.exe"

actions = [
    (516, 405, 4),
    (50, 100, 1),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (249, 203, 4),
    (447, 286, 4),
]

# --- Install dependencies if needed (run once) ---
# pip install --upgrade pyautogui pyscreeze pillow requests

print("Starting Avica automation...")

# Small delay at start
time.sleep(10)

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
                # Append to show.bat
                with open('show.bat', 'a', encoding='utf-8') as bat_file:
                    bat_file.write(f'\necho Avica Remote ID : {download_page}')
                print(f"Upload successful: {download_page}")
                return download_page
            else:
                print("Upload error:", result.get('status'))
                return None
    except Exception as e:
        print(f"Failed to upload image: {e}")
        return None

# Launch Avica properly
try:
    print(f"Launching: {avica_path}")
    subprocess.Popen([avica_path])
    time.sleep(8)  # Give Avica time to start
except Exception as e:
    print(f"Failed to launch Avica: {e}")
    sys.exit(1)

# Execute the click sequence
for x, y, duration in actions:
    try:
        pag.click(x, y, duration=duration)
        print(f"Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Click failed at ({x}, {y}): {e}")

    # Special handling for Allow Remote Access button
    if (x, y) == (249, 203):
        time.sleep(1.5)
        pag.click(x, y, duration=duration)  # Click again to be sure

    # Special handling near the end (launch + screenshot)
    if (x, y) == (447, 286):
        time.sleep(10)  # Extra wait

        try:
            print("Taking screenshot...")
            screenshot = pag.screenshot()
            screenshot.save(img_filename)
            print(f"Screenshot saved as {img_filename}")
        except Exception as e:
            print(f"Screenshot failed: {e}")
            print("This usually happens in headless environments (GitHub Actions, RDP without desktop, etc.)")
            # Create a dummy image so upload doesn't fail
            try:
                from PIL import Image, ImageDraw
                img = Image.new('RGB', (800, 600), color='black')
                draw = ImageDraw.Draw(img)
                draw.text((50, 50), "Screenshot failed - headless environment", fill='white')
                img.save(img_filename)
            except:
                pass

        # Upload
        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print(f"✅ Image uploaded: {gofile_link}")
        else:
            print("❌ Failed to upload image")

    time.sleep(8)  # Default delay between actions

print('Script finished!')
