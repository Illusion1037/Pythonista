from scene import *

class Cursor (object):
	def __init__(self, pos, color=(0, 0, 0)):
		self.x = pos[0]
		self.y = pos[1]
		
		self.color = color
	
	def set_pos(x, y):
		self.x = x
		self.y = y
		
	def set_color(r, g, b):
		self.color = (r, g, b)
	
	def get(self):
		return self.x, self.y, self.color
		
#class Button (object)
