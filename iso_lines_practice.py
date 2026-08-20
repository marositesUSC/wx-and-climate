# I need surface maps from a AMS Url
# It updates every hour, but both images are not available at the same time. 
# this script will download images every hour and save them to a folder. So that way I can have some options. 

import os
import requests
from datetime import datetime
import time

def download_image(url, folder_name="downloaded_images", name=''):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Get the current timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{folder_name}/{name}image_{timestamp}.gif"

        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded image and saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

isotherms_image_url = "https://edu.ametsoc.org/dstreme/images/sfc_temp.gif"

temperatures_image_url = "https://edu.ametsoc.org/dstreme/images/sfcptemp.gif"

i = 0
wait_time = 60*60 /2      # 60 minutes * 60 seconds

while i < 12:
    download_image(isotherms_image_url, name='iso_')
    download_image(temperatures_image_url, name='temp_')
    print(f'Waiting {wait_time} seconds...')
    time.sleep(wait_time)
    
