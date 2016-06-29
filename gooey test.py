from scene import *
from gooey import *

test = App()

class LeftBtn (button.DrawButton):
	def __init__(self):
		self.set_rect((5, 5, 50, 50))
	
	def on(self):
		color.set(color.blue)
		draw.ellipse((5, 5, 50, 50))
		color.set(color.white)
		draw.line((40, 15), (15, 30), 2)
		draw.line((15, 30), (40, 45), 2)
		
	#def up(self):
		#test.set_page(PageTwo())
		
	def off(self):
		color.set(color.white)
		draw.line((40, 15), (15, 30), 2)
		draw.line((15, 30), (40, 45), 2)

class Drawing (layer.Layer):
	
	def transform(self):
		self.rotate(-20)
		self.translate((0, 100))
		self.scale(0.75, 1.2)
		
	def main(self):
		
		color.set(color.orange)
		draw.rect((20, 20, 20, 20), 3, color.yellow)
		color.set(color.blue)
		draw.ellipse((200, 50, 40, 20), 2, color.red)
		color.set(color.violet)
		draw.poly(((50, 200), (70, 220), (90, 220), (70, 200)))
		color.set(color.white)
		draw.line((20, 100), (100, 20), 2)
		
class PageTwo (Page):
	
	def setup(self):
		self.set_header('Page 2', color.black, color.white)
		self.set_bgcolor(color.blue)
		
		self.leftbtn = LeftBtn()
		
	def main(self):
		self.leftbtn.draw()

class NewPage (Page):
	
	def setup(self):
		self.set_header('Wow!!!!!', color.cyan, color.black)
		self.set_bgcolor(color.green)
		
		self.button = button.TextButton('Click', (200, 200, 100, 30), 'Copperplate-Light', 16, 1, color.black, color.green, color.black, color.green, color.black, color.white)
		self.leftbtn = LeftBtn()
	
	def main(self):
		Drawing().draw()
		self.button.draw()
		self.leftbtn.draw()
		print self.leftbtn.get()
		
test.add(NewPage())
test.add(PageTwo())
		
start(test)
