from gooey import *
from scene import *

test = App()

class NewPage (Page):
	def setup(self):
		#self.toggle_header()
		self.button = button.TextButton('Test', (20, 20, 100, 40), (0, 1, 0))
		
	def main(self):
		#self.button.draw(test.touches.values())
		rect(40, 20, 20, 20)
		fill(1, 0.5, 0)
		stroke_weight(1)
		stroke(0, 0, 0)
		line(40, 40, 40, 60)
		line(40, 60, 60, 60)
		line(60, 60, 60, 40)
		line(60, 40, 40, 40)
		stroke_weight(0)
		
test.add_page(NewPage('Test', (0, 0, 1)))

start(test)
