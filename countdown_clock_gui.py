import PySimpleGUI as sg
from time import sleep
import os

sg.theme('DarkAmber')

timer = sg.Text("ok", background_color='black', font=('Helvetica', 40))

layout = [
    [sg.Text("Countdown Clock", background_color='black', font=('Helvetica', 40))],
    [sg.Frame("timer",layout = [[timer]])],
    [sg.Button("Start", font=('Helvetica', 20)),
    sg.Button("Reset", font=('Helvetica', 20)),
    sg.Button("Exit", font=('Helvetica', 20))],
    [sg.Multiline(size=(50, 2), key='textbox')]
]

window = sg.Window("Countdown Clock", layout,   
          margins=(300, 200), background_color='black', resizable=True, icon='Material/countdown_clock_gui/icon.ico')

def start():
    time = int(values['textbox'])
    while time > 0:
        
        hour = time // 3600

        minute = (time % 3600) // 60

        second = time - hour*3600 - minute*60

        time_string = "%02d : %02d : %02d" %(hour, minute, second)
        
        timer.Update(time_string)
        
        time -= 1
        
        sleep(1)

def reset():
    print("reset!")
    
while True:
    event, values = window.read()
    
    if event in (None, "Exit"):
        break
    elif event == "Start":
        start()
    elif event == "Reset":
        reset()
        
window.close()

