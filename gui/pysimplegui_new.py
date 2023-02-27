# Example from
# https://www.pysimplegui.org/en/latest/#install

import PySimpleGUI as sg
# EM 2.9.2022
# Tuve problemas instalando tkinter (no se dejaba instalar en el 3.10, version default).
# Lo instalé así:
"""
sudo apt-get update
sudo apt install python3-tk
"""

sg.popup('Pseudogene project', 'This is the shortest GUI program ever!')


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Find a pseudogene (psg)')],
            [sg.Text('Pseudogene name: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Pseudogenes', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        print('You entered nothing')
        break
    if event == 'Ok': # if user closes window or clicks cancel
        print('You entered \"', values[0], '\"', sep="")
        break


window.close()
