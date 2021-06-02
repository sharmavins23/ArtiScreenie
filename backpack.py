from helper.res import getScreenResData
from helper.img import takeShot, sendToClipboard
from helper.win32 import waitForT, pause

context = "backpack"


# Take one screenshot and send it to the clipboard
def takeOneScreenie():
    # First, get screen resolution
    data = getScreenResData(context)

    print("Press T when ready to take screenshot.")

    sendToClipboard(takeShot(data["TL"], data["OFF"]))


# Take continuous screenshots and send them to the clipboard
def takeContinuous():
    # First, get screen resolution
    screenData = getScreenResData(context)


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
