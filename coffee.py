"""
coffee.py
Keeps your computer awake!

A script that keeps your computer from sleeping by slightly moving the mouse once every 30 minutes

author: T. Emmons
"""

import pyautogui
import time
import random

def press_f15():

    print("""
    coffee.py
    Keep your computer up!

    This is an opensource python script modeled after caffeine.exe that keeps your computer awake even if there is an inactivity timer.
    Please use responsibly.
    
    author: T. Emmons
    """)

    while True:
        try:
            # Press an innocuous key
            pyautogui.press('f15')
            print("Key pressed!")
            wait_time = random.uniform(30, 59)
            time.sleep(wait_time)
        except Exception:
            print("Error")
        
if __name__ == "__main__":
    press_f15()
