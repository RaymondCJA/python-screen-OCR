import os
from dotenv import load_dotenv
from google.cloud import vision
from PIL import ImageGrab

# Load environment variables from .env file
load_dotenv()

def run_quickstart() -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Take a screenshot of a specific area on the screen
    # Set the coordinates (left, top, right, bottom) of the area to capture
    area = (30,30,215,151) # area = (left, top, right, bottom) in terms of coordinates
    screenshot = ImageGrab.grab(bbox=area)

    # Convert the screenshot to bytes
    with open("screenshot.png", "wb") as f:
        screenshot.save(f)
    
    # Read the screenshot from the local file
    with open("screenshot.png", "rb") as f:
        content = f.read()

    # Create a Vision API image from the screenshot bytes
    image = vision.Image(content=content)

    # Performs OCR (text detection) on the image
    response = client.text_detection(image=image)
    annotations = response.text_annotations

    return annotations

def main():
    annotations = run_quickstart()
    # print("Detected Text:")
    for annotation in annotations:
        print(annotation.description)

    # Optional: If you want to display the screenshot
    # ImageGrab.grab() captures the area defined in the run_quickstart() function.
    # The screenshot will be displayed using the default image viewer.
    # ImageGrab.grab(bbox=area).show()


if __name__ == "__main__":
    main()
