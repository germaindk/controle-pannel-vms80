import PySimpleGUI as sg
import RPi.GPIO as GPIO


#setup GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('Start'), sg.Button('Stop'), sg.Button('ex1'), sg.Button('ex2')],
            [sg.Button('test')] ]

# Create the Window
window = sg.Window('Controle pannel VMS80', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Start':
        print('Start')
    window.Refresh()    
window.close()
