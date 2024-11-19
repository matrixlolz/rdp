import pyautogui as pag
import time
import requests
import os


# Fixed By matrix
actions = [
    (516, 405, 4), 
    (50, 100, 1),   
    (249, 203, 4),  
    (249, 203, 4),  
    (249, 203, 4),  
    (249, 203, 4),  
    (447, 286, 4), 
]


time.sleep(10)


img_filename = 'Avicaidbymatrix.png'

# Upload to Gofile.io
def upload_image_to_gofile(img_filename):
    url = 'https://store1.gofile.io/uploadFile'
    try:
        with open(img_filename, 'rb') as img_file:
            files = {'file': img_file}
            response = requests.post(url, files=files)
            response.raise_for_status()  # Throws error for HTTP issues
            result = response.json()

            if result['status'] == 'ok':
                download_page = result['data']['downloadPage']
                with open('show.bat', 'a') as bat_file:
                    bat_file.write(f'\necho Avica Remote ID : {download_page}')
                return download_page
            else:
                print("Upload error:", result.get('status'))
                return None
    except Exception as e:
        print(f"Failed to upload image: {e}")
        return None

# Iterate through actions
for x, y, duration in actions:
    pag.click(x, y, duration=duration)
    if (x, y) == (249, 203):  # Attempt to activate "Allow remote access"
        time.sleep(1)  # Delay to ensure the button click registers
        pag.click(x, y, duration=duration)  # Try activating the button again
    
    if (x, y) == (447, 286):  # Launch avica and upload screenshot
        os.system('"C:\\Program Files x86\\Avica\\Avica.exe"')
        time.sleep(5)  # Give some time for the app to launch
        pag.click(249, 203, duration=4)  # Re-click on the Allow button coordinates
        time.sleep(10)  # Extra 10 seconds delay before taking the screenshot
        pag.screenshot().save(img_filename)
        gofile_link = upload_image_to_gofile(img_filename)
        if gofile_link:
            print(f"Image uploaded successfully. Link: {gofile_link}")
        else:
            print("Failed to upload the image.")
    time.sleep(10)

print('Done!')