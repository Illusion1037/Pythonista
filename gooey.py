from scene import *
import color, draw, layer, button

def start(app):
	run(app, app.orientation)

class App (Scene):
	def __init__(self, orientation=PORTRAIT):
		self.pages = []
		self.orientation = orientation
		
	def add(self, page):
		self.pages.append(page)
		page.set_app(self)
		
	def set_page(self, page):
		if page in self.pages:
			self.pages.remove(page)
		
		self.pages.insert(0, page)
		
	def setup(self):
		self.pages[0].init()
	
	def draw(self):
		button.touches = self.touches.values()
		self.pages[0].draw()
		
class Page (object):
	def __init__(self):
		self.title = 'New Page'
		self.color = (0, 0, 0)
		self.txtcolor = (1, 1, 1)
		self.bgcolor = (1, 1, 1)
		self.show_header = True
		self.orientation = PORTRAIT
		self.app = None
		
	def set_app(self, app):
		self.app = app
		self.orientation = app.orientation
		
	def set_title(self, title):
		self.title = title
		
	def set_color(self, color):
		self.color = color
		
	def set_bgcolor(self, bgcolor):
		self.bgcolor = bgcolor
	
	def set_txtcolor(self, txtcolor):
		self.txtcolor = txtcolor
		
	def set_header(self, title, color, txtcolor):
		self.title = title
		self.color = color
		self.txtcolor = txtcolor
	
	def toggle_header(self):
		if self.show_header:
			self.show_header = False
		else:
			self.show_header = True
			
	def init(self):
		try:
			self.setup()
		except AttributeError:
			pass
		
	def draw(self):
		background(self.bgcolor[0], self.bgcolor[1], self.bgcolor[2])
		
		try:
			self.main()
		except AttributeError:
			pass
		
		if self.show_header:
			stroke_weight(0)
			if self.orientation == PORTRAIT:
				
				fill(self.color[0], self.color[1], self.color[2])
				rect(0, 440, 320, 40)
				tint(self.txtcolor[0], self.txtcolor[1], self.txtcolor[2])
				text(str(self.title), 'AvenirNext-Regular', 24, 160, 460, 5)
				fill(0.60, 0.60, 0.60, 0.60)
				rect(0, 439.5, 320, 0.5)
				fill(0.5, 0.5, 0.5, 0.5)
				rect(0, 439, 320, 0.5)
				fill(0.4, 0.4, 0.4, 0.4)
				rect(0, 438.5, 320, 0.5)
				fill(0.3, 0.3, 0.3, 0.3)
				rect(0, 438, 320, 0.5)
				fill(0.2, 0.2, 0.2, 0.2)
				rect(0, 437.5, 320, 0.5)
				fill(0.1, 0.1, 0.1, 0.1)
				rect(0, 437, 320, 0.5)
				
			else:
				
				fill(self.color[0], self.color[1], self.color[2])
				rect(0, 280, 480, 40)
				tint(self.txtcolor[0], self.txtcolor[1], self.txtcolor[2])
				text(str(self.title), 'AvenirNext-Regular', 24, 240, 300, 5)
				fill(0.60, 0.60, 0.60, 0.60)
				rect(0, 279.5, 480, 0.5)
				fill(0.5, 0.5, 0.5, 0.5)
				rect(0, 279, 480, 0.5)
				fill(0.4, 0.4, 0.4, 0.4)
				rect(0, 278.5, 480, 0.5)
				fill(0.3, 0.3, 0.3, 0.3)
				rect(0, 278, 480, 0.5)
				fill(0.2, 0.2, 0.2, 0.2)
				rect(0, 277.5, 480, 0.5)
				fill(0.1, 0.1, 0.1, 0.1)
				rect(0, 277, 480, 0.5)
