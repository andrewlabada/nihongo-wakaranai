import PySimpleGUI as sg 

sg.theme("DarkAmber")

data = "あなた"
answer = "anata"
layout = [[sg.Text(data)],
          [sg.InputText(key='-ROMAJI-')],
          [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Nihongo Wakaranai', layout)

event, values = window.read()

window.close()

romaji = values['-ROMAJI-']

if romaji == answer:
    sg.popup('You are correct the answer is.', romaji)
else:
    sg.popup('You are not correct the answer is ', answer)




