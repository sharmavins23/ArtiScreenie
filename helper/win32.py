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


# Waits for a C or X key to continue or to exit
def waitForCX():
    while True:
        keyStateC = win32api.GetAsyncKeyState(ord("C"))  # C key VKEY state
        keyStateX = win32api.GetAsyncKeyState(ord("X"))  # X key VKEY state

        # print(keyStateC)  # DBG
        # print(keyStateX)  # DBG

        if keyStateC != 0:
            return "C"
        elif keyStateX != 0:
            return "X"


# Waits for a T or X key to take a shot or exit
def waitForTX():
    while True:
        keyStateT = win32api.GetAsyncKeyState(ord("T"))  # T key VKEY state
        keyStateX = win32api.GetAsyncKeyState(ord("X"))  # X key VKEY state

        # print(keyStateT)  # DBG
        # print(keyStateX)  # DBG

        if keyStateT != 0:
            return "T"
        elif keyStateX != 0:
            return "X"


# Waits for a T, N, or X key to take a shot, newline, or exit
def waitForTNX():
    while True:
        keyStateT = win32api.GetAsyncKeyState(ord("T"))  # T key VKEY state
        keyStateN = win32api.GetAsyncKeyState(ord("N"))  # N key VKEY state
        keyStateX = win32api.GetAsyncKeyState(ord("X"))  # X key VKEY state

        # print(keyStateT)  # DBG
        # print(keyStateN)  # DBG
        # print(keyStateX)  # DBG

        if keyStateT != 0:
            return "T"
        elif keyStateN != 0:
            return "N"
        elif keyStateX != 0:
            return "X"


# Waits for a standardized amount of time
def pause():
    time.sleep(0.1)
