import os             
import pyautogui
import time
from time import sleep
from datetime import datetime


try:
    # open MS Teams application
    os.startfile("C:/Users/a0f20d1/AppData/Local/Microsoft/Teams/current/Teams.exe") 
    sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'm')
except Exception as e:
    print(e)

