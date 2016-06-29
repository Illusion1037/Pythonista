#coding: utf-8

from scene import *
from time import sleep

class MyScene (Scene):
	def setup(self):
		self.keys = (('q w e r t y u i o p', 'a s d f g h j k l', 'Shift z x c v b n m Backspace', 'Numbers1 Space Enter'), \
		('1 2 3 4 5 6 7 8 9 0', '- / : ; ( ) $ & @ "', "Symbols . , ? ! ' Backspace", 'Alphabet Space Enter'), \
		('[ ] { } # % ^ * + =', '_ \ | ~ < > € £ ¥ •', 'Numbers2 . , ? ! Backspace', 'Alphabet Space Enter'))
		
		self.touch = Touch(0, 0, 0, 0, 0)
	
	def draw(self):
		
		def key(key, x, y):
			
			if key == 'Shift':
				pass
			
			elif key == 'Backspace':
				pass
				
			elif key == 'Numbers1':
				pass
			
			elif key == 'Space':
				pass
				
			elif key == 'Enter':
				pass
				
			elif key == 'Symbols':
				pass
				
			elif key == 'Alphabet':
				pass
				
			elif key == 'Numbers2':
				pass
				
			else:
				if x + 12.5 < 160:
					shadx = x + (160 - (x + 12.5)) / 40
					shadw = 25
				elif x + 12.5 > 160:
					shadx = x - ((x + 12.5) - 160) / 40
					shadw = 25
				else:
					shadx = x + (160 - (x + 12.5)) / 40
					shadw = (x - (x - 160) / 40) - x
					print shadx, shadw
				
				if self.touch in Rect(x, y, 25, 40):
					fill(0.5, 0.5, 0.5)
					rect(shadx, y - 4, 25, 36)
					tint(0, 0, 0)
					text(key, 'AvenirNext-UltraLight', 32, shadx + 12.5, y + 16)
					fill(1, 1, 1)
					rect(x - 5, y + 49, 35, 46)
					fill(0.5, 0.5, 0.5)
					rect(x - 5, y + 45, 35, 4)
					text(key, 'AvenirNext-UltraLight', 44, x + 12.5, y + 72)
				else:
					fill(0.7, 0.7, 0.7)
					rect(shadx, y - 4, shadw, 40)
					fill(1, 1, 1)
					rect(x, y, 25, 40)
					tint(0, 0, 0)
					text(key, 'AvenirNext-UltraLight', 32, x + 12.5, y + 20)
		
		def keyboard():
			
			self.alphabet = self.keys[0]
			
		background(0.9, 0.9, 0.9)
			
#		fill(1, 1, 1)
#		rect(20, 20, 25, 40)
#		tint(0, 0, 0)
#		text(unichr(163), 'AvenirNext-UltraLight', 32, 32.5, 40, 5)
		
		key('¥', 20, 20)
		key('•', 275, 20)
		key('€', 147.5, 20)
	
	def touch_began(self, touch):
		self.touch = touch.location
	
	def touch_moved(self, touch):
		self.touch = touch.location

	def touch_ended(self, touch):
		self.touch = Touch(0, 0, 0, 0, 0)

run(MyScene())
