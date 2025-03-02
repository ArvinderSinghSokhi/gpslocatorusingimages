import os
import subprocess
import webbrowser
import re

def get_gps_data(image_path):
    try:
        result = subprocess.run(['exiftool', '-GPSLatitude', '-GPSLongitude', image_path], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')

        if len(output) < 2:
            print(f"No GPS data found in {image_path}")
            return None, None

        print("Raw GPS Data:", output)

        # Use regex to clean extra spaces and extract coordinates
        lat = re.sub(r'\s+', ' ', output[0].split(': ')[1]).strip()
        lon = re.sub(r'\s+', ' ', output[1].split(': ')[1]).strip()

        lat = convert_to_decimal(lat)
        lon = convert_to_decimal(lon)
        
        return lat, lon
    except Exception as e:
        print(f"Error extracting GPS data: {e}")
        return None, None

def convert_to_decimal(coord):
    try:
        print(f"Converting: {coord}")

        # Remove unnecessary labels like "deg", "'", '"'
        coord = coord.replace('deg', '').replace("'", '').replace('"', '').strip()
        parts = re.split(r'\s+', coord)

        if len(parts) != 4:
            raise ValueError("Invalid coordinate format")

        degrees = float(parts[0])
        minutes = float(parts[1])
        seconds = float(parts[2])
        direction = parts[3]

        decimal = degrees + (minutes / 60) + (seconds / 3600)
        if direction in ['S', 'W']:
            decimal = -decimal
        
        return decimal
    except Exception as e:
        print(f"Error converting to decimal: {e}")
        return None

def open_google_maps(lat, lon):
    if lat is not None and lon is not None:
        url = f"https://www.google.com/maps?q={lat},{lon}"
        print(f"Opening Google Maps: {url}")
        webbrowser.open(url)
    else:
        print("Invalid coordinates, cannot open Google Maps.")

# Test on a single image
image_path = r"C:\Users\assok\OneDrive\Desktop\profile\DSCN0029.jpg"
lat, lon = get_gps_data(image_path)
open_google_maps(lat, lon)
