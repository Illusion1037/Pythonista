# coding: utf-8

import ui

def text_edit(sender):
	sender.text = 'Enter your name and then press the button'
def button_pressed():
	if textview.text == '':
		textview.text = 'Invalid input'
	else:
		textview.text = 'Hello '+name.text+'!'

ui.load_view('Greeting').present('Sheet')
