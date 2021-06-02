import pyautogui
from win32 import waitForT, playSound, pause
from PIL import Image
from functools import reduce

# Contains all helper screenshot code


# Takes a screenshot on T press
def takeShot(TL, OFF):
    waitForT()

    # Take a screenshot
    image = pyautogui.screenshot(region=TL+OFF)
    # Play notification sound
    playSound()
    pause()

    return image


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
    chunkList = []

    # Start by breaking image list into chunks of size 5 max
    while len(imgs) > 5:
        chunk = imgs[:5]  # Split off a chunk from the start
        imgs = imgs[5:]  # and cut off the remainder
        chunkList.append(chunk)

    chunkList.append(imgs)  # Append the remainder

    retImg = None
    # Iterate through chunklist and merge into images
    for chunk in chunkList:
        # Combine a chunk into a horizontal row of 5 artifacts
        chunkImg = reduce(concat2ImagesHoriz, chunk)

        if retImg is None:  # On first run, save this image
            retImg = chunkImg
        else:  # Otherwise, paste onto the bottom of this image
            retImg = concat2ImagesVerti(retImg, chunkImg)

    return retImg
