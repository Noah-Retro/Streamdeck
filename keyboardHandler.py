'''
Programm: 
    Modules:
        json, pyautogui, os, more can be added
'''
import json, os, pyautogui,webbrowser

from pynput.keyboard import Key, Listener

with open(os.getcwd() + "\config.json") as e:  #reads the json file
    data = json.load(e)

class KeyboardHandler():
    def __init__(self):
        pass
    def update(self):
        # Collect events until released
        with Listener(      
            on_press=self.on_press,
            on_release=self.on_release) as listener:
                listener.join()

    #debuging prints the key
    def on_press(self,key):
        pass

    #binds the written function in json to the buttons
    def on_release(self,key):
        try:
            if key == Key.f13:
                eval(data["f13"])
            if key == Key.f14:
                eval(data["f14"])
            if key == Key.f15:
                eval(data["f15"])
            if key == Key.f16:
                eval(data["f16"])
            if key == Key.f17:
                eval(data["f17"])
            if key == Key.f18:
                eval(data["f18"])
            if key == Key.f19:
                eval(data["f19"])
            if key == Key.f20:
                eval(data["f20"])
            if key == Key.f21:
                eval(data["f21"])
            if key == Key.f22:
                eval(data["f22"])
            if key == Key.f23:
                eval(data["f23"])
            if key == Key.f24:
                eval(data["f24"])

            #for debugging stops programm
            if key == Key.esc:
                # Stop listener
                return False
        except Exception as e:
            print("An exaption occurred: ", e)



if __name__ == '__main__':
    keyboardHandler = KeyboardHandler()
    keyboardHandler.update()
