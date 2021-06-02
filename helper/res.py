import pyautogui

# Screen resolution helper code


# Returns all screen resolution data
def getScreenResData(context):
    # Get our native screen resolution
    screenResolution = pyautogui.size()  # Returns (2560, 1440)

    # All box data
    screenResBoxes = {
        (2560, 1440): {
            'backpack': {
                'TL': (1723, 160),
                'BR': (2378, 1279)
            }
        }
    }

    # Sanity parameter check
    if screenResolution not in screenResBoxes.keys():
        raise ValueError("Size not supported.")

    return screenResBoxes[screenResolution][context]
