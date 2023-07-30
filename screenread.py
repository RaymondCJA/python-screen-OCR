import os
from dotenv import load_dotenv
from google.cloud import vision
from desktopmagic.screengrab_win32 import getRectAsImage
import keyboard
import clipboard

# Load environment variables from .env file
load_dotenv()

def run_quickstart() -> str:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Take a screenshot of a specific area on the screen
    area_standard_left_monitor = (-557, 94, -9, 270)
    screenshot = getRectAsImage(area_standard_left_monitor)

    # Save the screenshot to a file (temporary step)
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

    # Read the screenshot from the local file
    with open(screenshot_path, "rb") as f:
        content = f.read()

    # Create a Vision API image from the screenshot bytes
    image = vision.Image(content=content)

    # Performs OCR (text detection) on the image
    response = client.text_detection(image=image)

    # Get the full_text_annotation from the response
    full_text_annotation = response.full_text_annotation

    # Extract and return the original text
    original_text = full_text_annotation.text

    # Delete the temporary screenshot file
    os.remove(screenshot_path)

    return original_text

def main():
    print("Press 'F8' to perform OCR and display the result. Press 'Esc' to exit.")
    while True:
        if keyboard.is_pressed("F8"):
            original_text = run_quickstart()
            print("Detected Text:")
            print(original_text)

            # Set the detected text to the clipboard
            clipboard.copy(original_text)

            # Add a slight delay to avoid multiple OCR executions for a single key press
            keyboard.wait("F8", suppress=True)
        elif keyboard.is_pressed("Esc"):
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
