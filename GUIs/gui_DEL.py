import PySimpleGUI as sg

text1 = sg.popup_get_text('Title', 'Please input something')
# sg.popup('Results', 'The value returned from PopupGetText', text)
tex2 = sg.popup_get_text('Title', 'fsdfasdfsdafsdf input something')
sg.popup('Results', 'The value returned from PopupGetText', text)