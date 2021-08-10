from helper.res import getScreenResData
from helper.img import concatImages, concatImagesNoChunking, takeShot, sendToClipboard, takeShotNoWait
from helper.win32 import pause, waitForTNX, waitForTX

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
    fullImg = concatImages(images)

    # Send full image to the clipboard
    sendToClipboard(fullImg)
    print("Image processed on clipboard.")


# Take N screenshots, with user specified newlines, and send to clipboard
def takePScreenshots():
    # First, get screen resolution
    data = getScreenResData(context)
    pause()

    print("Press T to take a screenshot. Press X to stop and save. Press N for new line.")

    images = []
    currentLine = []  # Stores the current line of images
    imgCount = 0
    while True:
        # Process choice
        choice = waitForTNX()
        if choice == "X":
            break
        elif choice == "N":
            print("Line ended.")
            pause()  # Pause for keyboard state to decay
            images.append(currentLine)
            currentLine = []
            continue

        # Take the shot
        arti = takeShotNoWait(data["TL"], data["OFF"])
        imgCount += 1

        # Append it to the current line
        currentLine.append(arti)
        print("Screenshot taken.")
        print("Total: " + str(imgCount))

    # Finally, concatenate all images
    print("Concatenating...")
    # First, remove all empty lists
    images = [x for x in images if x]
    # Then, concatenate all images
    fullImg = concatImagesNoChunking(images)

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
    [p] N artifacts, with user-defined newlines
    [c] Continuous mode
Default 1: """
    )

    if choice == "1":
        takeOneScreenie()
    elif choice == "c":
        takeContinuous()
    elif choice == "p":
        takePScreenshots()
    else:
        takeNScreenshots()
