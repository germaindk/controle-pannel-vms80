import PySimpleGUI as sg
#import RPi.GPIO as GPIO
import time
import rtmidi



#setup midi
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
    print(midiout.open_port(0))



midiout.send_message("S")

#setup GPIO
#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)




def Blinck(PIN,timer):
    x = 0
    while x != timer:
        #GPIO.output(PIN, GPIO.LOW)
        time.sleep(1)
        #GPIO.output(PIN, GPIO.HIGH)
        time.sleep(1)
        #GPIO.output(PIN, GPIO.LOW)
        time.sleep(0.5)
        #GPIO.output(PIN, GPIO.HIGH)
        x = x + 1

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('Start'), sg.Button('Stop'), sg.Button('ECHO Key'), sg.Button('MARK'), sg.Button('Diameter Selection'), sg.Button('Display MODE')],
            [sg.Button('Fast'), sg.Button('Mark Time (0.6s)', key='_1_',button_color=('red')), sg.Button('Mark Time(0.8s)',key='_2_',button_color=('red')), sg.Button('Min Width (40um)',key='_5_',button_color=('red')), sg.Button('Min Width (50um)',key='_6_',button_color=('red'))],
            [sg.Button('Slow'),sg.Button('Mark Time (1.0s)', key='_3_',button_color=('red')), sg.Button('Mark Time(1.3s)',key='_4_',button_color=('red')), sg.Button('Min Witdh (60um)',key='_7_',button_color=('red')), sg.Button('Min Witdh (80um/off',key='_8_',button_color=('red'))],
            #switch state Button
            [sg.Button('2nd Deth On', button_color=('green'), key= '_2nd_'), sg.Button('Algorithm Fast',button_color=('green'), key='_algo_'), sg.Button('Economy ON', key = '_Eco_', button_color=('green')), sg.Button('Safety Groove On', button_color=('green'), key='_SaG_')] ]



eco_down = True
deth_down = True
algo_down = True
SaG_down = True

Mark_Time = 'false'
Min_Width = 'false'


# Create the Window
window = sg.Window('Controle pannel VMS80', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
#********************************************************************************************
    #Button switch
    if event == '_Eco_':
        eco_down = not eco_down
        window.Element('_Eco_').Update(('Economy Off', 'Economy On')[eco_down],
            button_color=(('red', 'green')[eco_down]))
    if event == '_2nd_':
        deth_down = not deth_down
        window.Element('_2nd_').Update(('2nd Deth Off', '2nd Deth On')[deth_down],
            button_color=(('red', 'green')[deth_down]))
    if event == '_algo_':
        algo_down = not algo_down
        window.Element('_algo_').Update(('Algorithm Slow', 'Algorithm Fast')[algo_down],
            button_color=(('red', 'green')[algo_down]))
    if event == '_SaG_':
        SaG_down = not SaG_down
        window.Element('_SaG_').Update(('Safety Groove Off', 'Safety Groove On')[SaG_down],
            button_color=(('red', 'green')[SaG_down]))
#**********************************************************************************************
    #Button Mark Time
    if event == '_1_':
        if Mark_Time == 'false':
            Mark_Time = '_1_'
            window.Element('_1_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_1_'
            window.Element('_1_').Update(button_color='green')
    
    if event == '_2_':
        if Mark_Time == 'false':
            Mark_Time = '_2_'
            window.Element('_2_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_2_'
            window.Element('_2_').Update(button_color='green')
    
    if event == '_3_':
        if Mark_Time == 'false':
            Mark_Time = '_3_'
            window.Element('_3_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_3_'
            window.Element('_3_').Update(button_color='green')
    
    if event == '_4_':
        if Mark_Time == 'false':
            Mark_Time = '_4_'
            window.Element('_4_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_4_'
            window.Element('_4_').Update(button_color='green')
#*********************************************************************************************
    #Button Min With
    if event == '_5_':
        if Min_Width == 'false':
            Min_Width = '_5_'
            window.Element('_5_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_5_'
            window.Element('_5_').Update(button_color='green')
    
    if event == '_6_':
        if Min_Width == 'false':
            Min_Width = '_6_'
            window.Element('_6_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_6_'
            window.Element('_6_').Update(button_color='green')
    
    if event == '_7_':
        if Min_Width == 'false':
            Min_Width = '_7_'
            window.Element('_7_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_7_'
            window.Element('_7_').Update(button_color='green')
    
    if event == '_8_':
        if Min_Width == 'false':
            Min_Width = '_8_'
            window.Element('_8_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_8_'
            window.Element('_8_').Update(button_color='green')

window.Refresh()    
window.close()
#GPIO.cleanup()