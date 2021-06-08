import PySimpleGUI as sg                        # Part 1 - The import
import json, os

description = """Das Programm führt die Befehle in den Zeilen aus.
Auch wen dieses Fenster geschlossen wird, werden die Befehle weiter ausgeführt. Alle Tastenanschläge werden aufgenommen.

Für die Befehle stehen json, os, pyautogui, webbrowser, pynput.keyboard als Packete zu Verfühgung. Es sind bis jetzt nur ein Zeilige Befehle möglich.
"""

TEXTBOX_SIZE= (100,2)

def start():
    with open(os.getcwd() + "\config.json") as e:    #reads the json file
        oData = json.load(e)

    # Define the window's contents
    layout = [  [sg.Multiline(key='test',size = (100,10),default_text=description)],                  # Part 2 - The Layout
                [sg.Multiline(key='f13',default_text= oData['f13'],size=TEXTBOX_SIZE)],[sg.Multiline(key='f14',default_text= oData['f14'],size=TEXTBOX_SIZE)],
                [sg.Multiline(key='f15',default_text= oData['f15'],size=TEXTBOX_SIZE)],[sg.Multiline(key='f16',default_text= oData['f16'],size=TEXTBOX_SIZE)],
                [sg.Multiline(key='f17',default_text= oData['f17'],size=TEXTBOX_SIZE)],[sg.Multiline(key='f18',default_text= oData['f18'],size=TEXTBOX_SIZE)],
                [sg.Multiline(key='f19',default_text= oData['f19'],size=TEXTBOX_SIZE)],[sg.Multiline(key='f20',default_text= oData['f20'],size=TEXTBOX_SIZE)],
                [sg.Multiline(key='f21',default_text= oData['f21'],size=TEXTBOX_SIZE)],[sg.Multiline(key='f22',default_text= oData['f22'],size=TEXTBOX_SIZE)],
                [sg.Multiline(key='f23',default_text= oData['f23'],size=TEXTBOX_SIZE)],[sg.Multiline(key='f24',default_text= oData['f24'],size=TEXTBOX_SIZE)],
                [sg.Button('Update'), sg.Button('Quit'),sg.Button('Delete Config'),sg.FileBrowse('Load Config',key='Save')]]

    # Create the window
    window = sg.Window('Config Editor', layout)      # Part 3 - Window Defintion

    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        if event == 'Update':
            data = {
                'f13':values['f13'],
                'f14':values['f14'],
                'f15':values['f15'],
                'f16':values['f16'],
                'f17':values['f17'],
                'f18':values['f18'],
                'f19':values['f19'],
                'f20':values['f20'],
                'f21':values['f21'],
                'f22':values['f22'],
                'f23':values['f23'],
                'f24':values['f24'],
            }
            with open(os.getcwd() + "\config.json",'w') as u:  #reads the json file
                json.dump(data,u,indent=2)
            
        if event == 'Load Config':
            pass
            
        

    # Finish up by removing from the screen
    window.close()                                  # Part 5 - Close the Window


if __name__ == '__main__':
    start()