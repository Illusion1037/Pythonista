import ui
view = ui.View()

def init_ui():
	import ui
	view = ui.View()
	
def display(uiName=''):
	view = ui.View()
	if uiName == '':
		view.present('sheet')
	else:
		ui.load_view(uiName).present('sheet')
