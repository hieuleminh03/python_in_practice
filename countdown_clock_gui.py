import PySimpleGUI as sg

window = sg.Window(layout=[[]], title="Countdown Clock",  
          margins=(600, 400), background_color='black', resizable=True, icon='Material/clockGUI/icon.ico')
window.read()

print("ok")