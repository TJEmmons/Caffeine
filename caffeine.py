"""
caffeine.py
Keeps your computer awake!

A script that keeps your computer from sleeping by slightly moving the mouse once every 30 minutes

author: T. Emmons
"""

import pyautogui
import time

# Get the current mouse position
x, y = pyautogui.position()

def move_mouse():
    """
    A function that moves the mouse slightly and then return it to its original position every 30 minutes.
    """
    while True:
        # Move the mouse slightly
        pyautogui.moveRel(-4, -4, duration=0.1)

        # Move the mouse back to its original position
        pyautogui.moveRel(4, 4, duration=0.1)

        # Wait 30 minutes
        time.sleep(1800)

if __name__ == "__main__":
    move_mouse()
