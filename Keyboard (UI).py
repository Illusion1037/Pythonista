# coding: utf-8

import ui

text1 = 'Type here'
text2 = ''
text3 = ''
text4 = ''
caps = False
letter = 0
line = 1

def button_clicked(sender):
	global text1, text2, text3, text4, line, caps, letter
	if letter == 1 and caps == True:
		letter = 0
		caps = False
		v['caps'].background_color = '#C8C8C8'
	elif caps == False:
		letter == 1
		
	if sender.name == 'space':
		if line == 1:
			text1 += ' '
		elif line == 2:
			text2 += ' '
		elif line == 3:
			text3 += ' '
		elif line == 4:
			text4 += ' '
	elif sender.name == 'enter' and line != 4:
		line += 1
	elif sender.name == 'backspace':
		if line == 1 and text1 != '':
			text1 = text1[:len(text1) - 1]
		elif line == 2 and text2 != '':
			text2 = text2[:len(text2) - 1]
		elif line == 2:
			text2 = ''
			line -= 1
		elif line == 3 and text3 != '':
			text3 = text3[:len(text3) - 1]
		elif line == 3:
			text3 = ''
			line -= 1
		elif line == 4 and text4 != '':
			text4 = text4[:len(text4) - 1]
		elif line == 4:
			text4 = ''
			line -= 1
	elif sender.name == 'caps':
		if caps == 0:
			caps = 1
			v['caps'].background_color = '#FFFFFF'
		else:
			caps = 0
			v['caps'].background_color = '#C8C8C8'
	else:
		if caps == 1:
			if line == 1:
				text1 += sender.name.upper()
			elif line == 2:
				text2 += sender.name.upper()
			elif line == 3:
				text3 += sender.name.upper()
			elif line == 4:
				text4 += sender.name.upper()
		else:
			if line == 1:
				text1 += sender.name
			elif line == 2:
				text2 += sender.name
			elif line == 3:
				text3 += sender.name
			elif line == 4:
				text4 += sender.name
		
v = ui.load_view('Keyboard (UI)')
v.present(orientations=['portrait'])

while True:
	textlabel1 = v['text1']
	textlabel2 = v['text2']
	textlabel3 = v['text3']
	textlabel4 = v['text4']
	if line == 1:
		textlabel1.text = text1 + '|'
		textlabel2.text = text2
		textlabel3.text = text3
		textlabel4.text = text4
	elif line == 2:
		textlabel2.text = text2 + '|'
		textlabel1.text = text1
		textlabel3.text = text3
		textlabel4.text = text4
	elif line == 3:
		textlabel3.text = text3 + '|'
		textlabel2.text = text2
		textlabel1.text = text1
		textlabel4.text = text4
	elif line == 4:
		textlabel4.text = text4 + '|'
		textlabel2.text = text2
		textlabel3.text = text3
		textlabel1.text = text1
