"""
requiert packegess 
    pyautogui
To Do:
1.X Keyboardhandler must be a thread by it self
2. get the UI ready -> PyQt5
"""
import threading
import time
import keyboardHandler
import settingsUI


kHandler = keyboardHandler.KeyboardHandler()
    

threading.Thread(target=settingsUI.start).start()
threading.Thread(target = kHandler.update).start()