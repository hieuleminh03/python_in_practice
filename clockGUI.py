import PySimpleGUI as sg

layout = []

window = sg.Window(layout, title="Countdown Clock",  
          margins=(600, 400), background_color='black', resizable=True, icon='icon.ico')

window.read()