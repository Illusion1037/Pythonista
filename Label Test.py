import ui
import console

v = ui.load_view('Label Test')
v.present('sheet')

def entername():
    mytext = console.input_alert('Please enter text:')
    textlabel = v['textlabel']
    textlabel.text = mytext

entername()
