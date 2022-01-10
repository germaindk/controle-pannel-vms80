import PySimpleGUI as sg
import RPi.GPIO as GPIO
import time

#setup GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)




def Blinck(PIN,timer):
    

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
    if event == 'test':
        print('Test')
        timer = 5
        x = 0
        while x != timer:
            GPIO.output(PIN, GPIO.LOW)
            time.sleep(1)
            GPIO.output(PIN, GPIO.HIGH)
            x = x + 1
        #Blinck(12,2)
    window.Refresh()    
window.close()
GPIO.cleanup()