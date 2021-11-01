# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script for creating an GUI


import PySimpleGUI as sg


def GUI_password_encoder():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Please enter the initial password: '), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Password encoder GUI', layout, enable_close_attempted_event=True)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Cancel') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
        print('You entered ', values[0])
    window.close()


def GUI_password_decoder():
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [[sg.Text('Please select encoded password file')],
              [sg.Input(), sg.FileBrowse()],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Password decoder GUI', layout, enable_close_attempted_event=True)

    while True:
        event, values = window.read()
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Cancel') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
    window.close()


GUI_password_decoder()
