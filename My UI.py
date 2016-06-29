import ui

def input(sender):
	if sender.name == 'go':
		textfield = v['textfield1']
		text = textfield.text
		textfield.end_editing()
		textlabel = v['textlabel']
		textlabel.text = text
		
v = ui.load_view('My UI')
v.present('sheet')
