import pyautogui
from helper.win32 import waitForT, pause
from PIL import Image
from functools import reduce
from io import BytesIO
import win32clipboard

# Contains all helper screenshot code


# Takes a screenshot on T press
def takeShot(TL, OFF):
    waitForT()

    # Take a screenshot
    image = pyautogui.screenshot(region=TL+OFF)
    pause()

    return image


# Takes a screenshot without wait
def takeShotNoWait(TL, OFF):
    image = pyautogui.screenshot(region=TL+OFF)
    pause()

    return image


# Splits a list of images into chunks of size n
def listToChunks(images, n):
    return [images[i:i + n] for i in range(0, len(images), n)]


# Concatenate two images together horizontally
def concat2ImagesHoriz(image1, image2):
    image = Image.new("RGB", (image1.width + image2.width, image1.height))
    image.paste(image1, (0, 0))
    image.paste(image2, (image1.width, 0))
    return image


# Concatenate two images together vertically
def concat2ImagesVerti(image1, image2):
    image = Image.new("RGB", (image1.width, image1.height + image2.height))
    image.paste(image1, (0, 0))
    image.paste(image2, (0, image1.height))
    return image


# Concatenate many images together
def concatImages(imgs):
    imgs = listToChunks(imgs, 5)

    # Concatenate all images and return
    return reduce(concat2ImagesVerti, [reduce(concat2ImagesHoriz, row) for row in imgs])


# Send the current image data to the Windows clipboard
def sendToClipboard(image):
    # Convert Image object into BMP bytestream
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    # Send to clipboard
    win32clipboard.OpenClipboard()  # Initialize reference
    win32clipboard.EmptyClipboard()  # remove current data
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
