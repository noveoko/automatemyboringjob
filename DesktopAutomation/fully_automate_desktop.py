import pyautogui
from time import sleep
import pytesseract
from pytesseract import Output
import argparse
import cv2

import pyttsx3


def say_this(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


def click_on_coords_of_text_in_image(image_path, text_to_find):
    # load the input image, convert it from BGR to RGB channel ordering,
    # and use Tesseract to localize each area of text in the input image
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

    # loop over each of the individual text localizations
    for i in range(0, len(results["text"])):
        # extract the bounding box coordinates of the text region from
        # the current result
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        # extract the OCR text itself along with the confidence of the
        # text localization
        text = results["text"][i]
        conf = int(results["conf"][i])

        if text_to_find in text.lower():
            # click on the found text
            pyautogui.click(x, y)


pyautogui.hotkey("winleft")
pyautogui.typewrite("chrome\n", 0.25)

sleep(1)

# take screenshot of entire screen and save it to file
pyautogui.screenshot("screenshot.png")

sleep(1)
say_this("Welcome to Chrome")
click_on_coords_of_text_in_image("screenshot.png", "marcin")

# add url to address bar in chrome
pyautogui.typewrite("https://reddit.com/r/machinelearning", 0.25)
# press enter
pyautogui.press("enter")
