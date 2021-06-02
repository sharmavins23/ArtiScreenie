import win32api
import time

# Contains all helper keyboard code


# Waits for a T input before returning
def waitForT():
    while True:
        keyState = win32api.GetAsyncKeyState(ord("T"))  # T key VKEY state

        # print(keyState)  # DBG

        if keyState != 0:
            return


# Waits for a standardized amount of time
def pause():
    time.sleep(0.1)
