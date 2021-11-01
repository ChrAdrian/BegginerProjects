# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script for creating an GUI


import PySimpleGUI as sg
import PasswordEncoder


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
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Cancel') \
                and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
        elif event == "Ok":
            new_string, rand_string = PasswordEncoder.generate_password(values)
            PasswordEncoder.write_password_to_file(new_string, rand_string)

        #print('You entered ', values[0])
    window.close()


def GUI_password_decoder():
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [[sg.Text('Please select encoded password file')],
              [sg.Input(), sg.FileBrowse()],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Password decoder GUI', layout, enable_close_attempted_event=True)

    while True:
        event, values = window.read()
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Cancel') \
                and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
    window.close()


def widgets_ex():
    sg.ChangeLookAndFeel('GreenTan')

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
                ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Help', '&About...'], ]

    # ------ Column Definition ------ #
    column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Text('(Almost) All widgets in one Window!', size=(30, 1), justification='center', font=("Helvetica", 25),
                 relief=sg.RELIEF_RIDGE)],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Frame(layout=[
            [sg.Checkbox('Checkbox', size=(10, 1)), sg.Checkbox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
             sg.Radio('My second Radio!', "RADIO1")]], title='Options', title_color='red', relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags')],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.Multiline(default_text='A second multi-line', size=(35, 3))],
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Frame('Labelled Group', [[
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sg.Column(column1, background_color='lightblue')]])],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

    window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)
    event, values = window.read()
    window.close()

    sg.Popup('Title',
             'The results of the window.',
             'The button clicked was "{}"'.format(event),
             'The values are', values)


# GUI_password_decoder()
GUI_password_encoder()
# event_loop_ex()