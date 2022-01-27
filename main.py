import PySimpleGUI as sg
import time
import serial

#setup connexion arduino

#serialPort = serial.Serial(port="", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
time.sleep(2) #wait 2 sec to let arduino conect 


#variable pour envoiller les commande
START = "s"
STOP = "p"
ECHO_Key= "k"
MARK = "m"
FAST = "f"
Dislay_MODE = "d"
Diameter_Selection = "D"
Safty_Groove = "g"

Algorithm_Fast = "A"
Algorithm_Slow = "a"

Economy_ON = "E"
Economy_off = "e"

Depth_ON = "N"
Depth_off = "n"

Mark_Time_1 = "1"
Mark_Time_2 = "2"
Mark_Time_3 = "3"
Mark_Time_4 = "4"

Min_Width_1 = "5" 
Min_Width_2 = "6"
Min_Width_3 = "7"
Min_Width_4 = "8"


button_size = (17,4)
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('Start',size=(button_size)), sg.Button('ECHO Key',size=(button_size)), sg.Button('MARK',size=(button_size)), sg.Button('Display MODE',size=(button_size)), sg.Button('Diameter Selection',size=(button_size))],
            [sg.Button('Stop',size=(button_size)), sg.Button('Mark Time (0.6s)', key='_1_',button_color=('red'),size=(button_size)), sg.Button('Mark Time(0.8s)',key='_2_',button_color=('red'),size=(button_size)), sg.Button('Min Width (40um)',key='_5_',button_color=('red'),size=(button_size)), sg.Button('Min Width (50um)',key='_6_',button_color=('red'),size=(button_size))],
            [sg.Button('Fast',size=(button_size)),sg.Button('Mark Time (1.0s)', key='_3_',button_color=('red'),size=(button_size)), sg.Button('Mark Time(1.3s)',key='_4_',button_color=('red'),size=(button_size)), sg.Button('Min Witdh (60um)',key='_7_',button_color=('red'),size=(button_size)), sg.Button('Min Witdh (80um/off',key='_8_',button_color=('red'),size=(button_size))],
            #switch state Button
            [sg.Button('2nd Deth On', button_color=('green'), key= '_2nd_',size=(button_size)), sg.Button('Economy ON', key = '_Eco_', button_color=('green'),size=(button_size)), sg.Button('Algorithm Fast',button_color=('green'), key='_algo_',size=(button_size)), sg.Button('Safety Groove On', button_color=('green'), key='_SaG_',size=(button_size))] ]


#variable pour les bouton switch
eco_down = True
deth_down = True
algo_down = True
SaG_down = True

#variable pour group de bouton
Mark_Time = 'false'
Min_Width = 'false'


# Create the Window
window = sg.Window('Controle pannel VMS80', layout, size =(800,480))
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
        serialPort.write(bytes((Economy_off,Economy_ON)[eco_down], 'utf-8'))
    if event == '_2nd_':
        deth_down = not deth_down
        window.Element('_2nd_').Update(('2nd Deth Off', '2nd Deth On')[deth_down],
            button_color=(('red', 'green')[deth_down]))
        serialPort.write(bytes((Depth_off,Depth_ON)[deth_down], 'utf-8'))
    if event == '_algo_':
        algo_down = not algo_down
        window.Element('_algo_').Update(('Algorithm Slow', 'Algorithm Fast')[algo_down],
            button_color=(('red', 'green')[algo_down]))
        serialPort.write(bytes((Algorithm_Slow,Algorithm_Fast)[algo_down], 'utf-8'))
    if event == '_SaG_':
        SaG_down = not SaG_down
        window.Element('_SaG_').Update(('Safety Groove Off', 'Safety Groove On')[SaG_down],
            button_color=(('red', 'green')[SaG_down]))
        serialPort.write(bytes(Safty_Groove, 'utf-8'))
#**********************************************************************************************
    #Button Mark Time
    if event == '_1_':
        if Mark_Time == 'false':
            Mark_Time = '_1_'
            serialPort.write(bytes(Mark_Time_1, 'utf-8'))
            window.Element('_1_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_1_'
            serialPort.write(bytes(Mark_Time_1, 'utf-8'))
            window.Element('_1_').Update(button_color='green')
    
    if event == '_2_':
        if Mark_Time == 'false':
            Mark_Time = '_2_'
            serialPort.write(bytes(Mark_Time_2, 'utf-8'))
            window.Element('_2_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_2_'
            serialPort.write(bytes(Mark_Time_2, 'utf-8'))
            window.Element('_2_').Update(button_color='green')
    
    if event == '_3_':
        if Mark_Time == 'false':
            Mark_Time = '_3_'
            serialPort.write(bytes(Mark_Time_3, 'utf-8'))
            window.Element('_3_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_3_'
            serialPort.write(bytes(Mark_Time_3, 'utf-8'))
            window.Element('_3_').Update(button_color='green')
    
    if event == '_4_':
        if Mark_Time == 'false':
            Mark_Time = '_4_'
            serialPort.write(bytes(Mark_Time_4, 'utf-8'))
            window.Element('_4_').Update(button_color=('green'))
        else:
            window.Element(Mark_Time).Update(button_color=('red'))
            Mark_Time = '_4_'
            serialPort.write(bytes(Mark_Time_4, 'utf-8'))
            window.Element('_4_').Update(button_color='green')
#*********************************************************************************************
    #Button Min With
    if event == '_5_':
        if Min_Width == 'false':
            Min_Width = '_5_'
            serialPort.write(bytes(Min_Width_1, 'utf-8'))
            window.Element('_5_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_5_'
            serialPort.write(bytes(Min_Width_1, 'utf-8'))
            window.Element('_5_').Update(button_color='green')
    
    if event == '_6_':
        if Min_Width == 'false':
            Min_Width = '_6_'
            serialPort.write(bytes(Min_Width_2, 'utf-8'))
            window.Element('_6_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_6_'
            serialPort.write(bytes(Min_Width_2, 'utf-8'))
            window.Element('_6_').Update(button_color='green')
    
    if event == '_7_':
        if Min_Width == 'false':
            Min_Width = '_7_'
            serialPort.write(bytes(Min_Width_3, 'utf-8'))
            window.Element('_7_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_7_'
            serialPort.write(bytes(Min_Width_3, 'utf-8'))
            window.Element('_7_').Update(button_color='green')
    
    if event == '_8_':
        if Min_Width == 'false':
            Min_Width = '_8_'
            serialPort.write(bytes(Min_Width_4, 'utf-8'))
            window.Element('_8_').Update(button_color=('green'))
        else:
            window.Element(Min_Width).Update(button_color=('red'))
            Min_Width = '_8_'
            serialPort.write(bytes(Min_Width_4, 'utf-8'))
            window.Element('_8_').Update(button_color='green')
#*******************************************************************************************
#Button
    if event == 'start':
        serialPort.write(bytes(START, 'utf-8'))
    if envent == 'stop':
        serialPort.write(bytes(STOP, 'utf-8'))
    if envent == 'ECHO Key':
        serialPort.write(bytes(ECHO_Key, 'utf-8'))
    if envent == 'MARK':
        serialPort.write(bytes(MARK, 'utf-8'))
    if envent == 'Fast':
        serialPort.write(bytes(FAST, 'utf-8'))
    if envent == 'Display MODE':
        serialPort.write(bytes(Dislay_MODE, 'utf-8'))
    if envent == 'Diameter Selection':
        serialPort.write(bytes(Diameter_Selection,'utf-8'))


window.Refresh()    
window.close()
