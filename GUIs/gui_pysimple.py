import PySimpleGUI as sg

sg.theme('LightGray1')	# Add a touch of color
# All the stuff inside your window.
# layout = [  [sg.Text('Amazon Search')],
#             [sg.Text('Name of Google WorkSheet'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

layout = [   [sg.Text('Name of Google WorkSheet', font='Verdana 12')],
            [sg.InputText(font='Verdana 12')],
            # [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text('Search Keyword', font='Courier 12')],
            [sg.InputText(font='Times 12')],
            [sg.Button('Ok', font='Times 12'), sg.Button('Cancel', font='Times 12')] ]

# Create the Window
window = sg.Window('Amazon Search', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        exit()        
    # print('You entered ', values[0])
    # sg.theme_previewer()


print("wwwwwwwwwwwwwwwwwwww")

window.close()
