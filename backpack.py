from functools import reduce
from helper.res import getScreenResData
from helper.img import concat2ImagesHoriz, concat2ImagesVerti, takeShot, sendToClipboard, listToChunks, takeShotNoWait
from helper.win32 import pause, waitForTX

context = "backpack"


# Take one screenshot and send it to the clipboard
def takeOneScreenie():
    # First, get screen resolution
    data = getScreenResData(context)
    pause()

    print("Press T when ready to take screenshot.")

    sendToClipboard(takeShot(data["TL"], data["OFF"]))


# Take continuous screenshots and send them to the clipboard
def takeContinuous():
    # First, get screen resolution
    data = getScreenResData(context)
    pause()

    print("Press T to take a screenshot.")

    while True:
        sendToClipboard(takeShot(data["TL"], data["OFF"]))
        print("Screenshot taken.")


# Take N screenshots, combine, and send to clipboard
def takeNScreenshots():
    # First, get screen resolution
    data = getScreenResData(context)
    pause()

    print("Press T to take a screenshot. Press X to stop and save.")

    images = []
    while True:
        # Process choice
        choice = waitForTX()
        if choice == "X":
            break

        # Take the shot
        arti = takeShotNoWait(data["TL"], data["OFF"])

        # Append it to the list
        images.append(arti)
        print("Screenshot taken.")
        print("Total: " + str(len(images)))

    # Finally, concatenate all images
    print("Concatenating...")
    # First, split array into chunks of 5 or less (rows of images)
    images = listToChunks(images, 5)
    # Concatenate the full image from the rows
    fullImg = reduce(
        concat2ImagesVerti,
        [reduce(concat2ImagesHoriz, row) for row in images]
    )

    # Send full image to the clipboard
    sendToClipboard(fullImg)
    print("Image processed on clipboard.")


# Driver code
if __name__ == "__main__":
    print("Screenshot tool - Backpack edition")
    print("How many artifacts would you like to screenshot?")

    choice = input(
        """    [1] One artifact
    [n] N artifacts (any number)
    [c] Continuous mode
Default 1: """
    )

    if choice == "1":
        takeOneScreenie()
    elif choice == "c":
        takeContinuous()
    else:
        takeNScreenshots()
