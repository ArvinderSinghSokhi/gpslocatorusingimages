# gpslocatorusingimages

## Overview
This project extracts metadata from image files using **ExifTool** and retrieves the GPS coordinates (latitude and longitude) embedded in the images. The extracted coordinates are converted into decimal format and used to open the exact location on Google Maps.

## How It Works
1. **Metadata Extraction:** The program uses ExifTool to extract GPS data, specifically the `GPS Latitude` and `GPS Longitude` tags.
2. **Data Conversion:** The extracted GPS coordinates (in degrees, minutes, and seconds format) are converted into floating-point decimal values for better readability and compatibility.
3. **Google Maps Integration:** The converted latitude and longitude values are fed into Google Maps, opening a browser window to pinpoint the exact location.

## Usage
1. **Ensure ExifTool is installed:**
   ```bash
   exiftool -ver
   ```
2. **Run the Python script:**
   ```bash
   python script.py
   ```
3. **Add your image path:**
   Update the `image_path` variable in the script with the correct path to your image.

## Example
If an image contains the following GPS metadata:
```
GPS Latitude                    : 43 deg 28' 5.68" N
GPS Longitude                   : 11 deg 52' 48.62" E
```
The program will convert these to decimal format and open Google Maps at:
```
https://www.google.com/maps?q=43.468244,11.880172
```

## Dependencies
- Python 3
- ExifTool

## Installation
1. Install **ExifTool**:
   - **Windows:** Download from [ExifTool official website](https://exiftool.org/)
   - **Mac/Linux:**
   ```bash
   sudo apt-get install libimage-exiftool-perl
   ```
2. Ensure Python is installed:
   ```bash
   python --version
   ```

## Contributing
Feel free to fork this project, submit pull requests, or report issues. Let’s make this better together!

---

Happy mapping! 🌍
