# python-screen-OCR
# ScreenOCR - Python Optical Character Recognition (OCR) Utility

ScreenOCR is a Python application that utilizes the Google Cloud Vision library to perform Optical Character Recognition (OCR) on text displayed on the screen, specifically capturing closed captions, and converting it into a readily copy-pastable format.

## Core Setup Steps

Before using ScreenOCR, follow these setup steps:

1. **Google Cloud Vision Credentials**: Obtain your Google Cloud Vision API credentials and store the path to the credentials JSON file in a `.env` file.

2. **Install Dependencies**: Ensure you have the required dependencies installed. You can install them using the following commands:

```
pip install --upgrade google-cloud-vision
pip install python-dotenv
pip install Desktopmagic
pip install keyboard
```

## How ScreenOCR Works

ScreenOCR takes a screenshot of a specified area on the screen (e.g., closed captions displayed in a video or livestream) and sends the captured image to the Google Cloud Vision API for OCR processing. The resulting text annotations are then extracted and presented in a format that can be easily copied and pasted for further use.
ScreenOCR also listens for a specific key press (default: F8) to trigger the OCR process. When the key is pressed, it captures the specified area on the screen using Desktopmagic, sends the image to the Google Cloud Vision API for OCR processing, and copies the detected text to the clipboard. You can then paste the detected text into other applications.

## Getting Started

1. Clone this repository to your local machine:

```
git clone https://github.com/RaymondCJA/python-screen-OCR
cd python-screen-OCR
```


2. Set up your `.env` file: Create a `.env` file in the root of the project and add the following line, replacing `/path/to/your/keyfile.json` with the actual path to your Google Cloud Vision credentials JSON file:

```
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/keyfile.json
```

3. Run ScreenOCR: Execute the Python script to start using ScreenOCR:

```
python screenread.py
```

4. Run functionality: Press the configured key (default: F8) to trigger OCR and copy the detected text to the clipboard, as well as to generate it on the console:

## Customization
You can customize the behavior of ScreenOCR by changing the following parameters in screenread.py:

area_standard_left_monitor: Adjust the coordinates to capture a different area on the screen.
keyboard.is_pressed("F8"): Change the key to trigger the OCR process. Replace "F8" with the desired key name.

## Contributing

We welcome contributions to improve and expand the capabilities of ScreenOCR. If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/). Feel free to use, modify, and distribute it according to the terms of the license.
