import scene

touches = []

class TextButton (object):
	
	def __init__(self, text, rect, font='AvenirNext-Regular', fontsize=16, bordrw=0, color=(0, 0, 0), txtcolor=(1, 1, 1), bordrcolor=(1, 1, 1), altcolor=(1, 1, 1), alttxtcolor=(0, 0, 0), altbordrcolor=(0, 0, 0)):
		self.text = text
		self.font = font
		self.fontsize = fontsize
		
		self.rect = rect
		
		self.bordrw = bordrw
		
		self.color = color
		self.txtcolor = txtcolor
		self.bordrcolor = bordrcolor
		self.altcolor = altcolor
		self.alttxtcolor = alttxtcolor
		self.altbordrcolor = altbordrcolor
		
		self.mode = 'off'
		self.prevmode = 'off'
		
	def set_text(self, text):
		self.text = text
		
	def set_rect(self, rect):
		self.rect = rect
		
	def get(self):
		return self.mode
		
	def draw(self):
		self.prevmode = self.mode
		self.mode = 'off'
		for touch in touches:
			if touch.location in scene.Rect(*self.rect):
				self.mode = 'on'
			elif self.prevmode == 'on':
				self.mode = 'up'
				
		if self.mode == 'on':
			scene.fill(*self.altcolor)
			scene.tint(*self.alttxtcolor)
			scene.stroke(*self.altbordrcolor)
		else:
			scene.fill(*self.color)
			scene.tint(*self.txtcolor)
			scene.stroke(*self.bordrcolor)
		
		scene.stroke_weight(self.bordrw)
		scene.rect(*self.rect)
		scene.text(self.text, self.font, self.fontsize, self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2)
		
class DrawButton (object):
	
	def __init__(self):
		self.mode = 'off'
		#self.prevmode = 'off'
		
	def set_rect(self, rect):
		self.rect = rect
	
	def get(self):
		return self.mode
		
	def draw(self):
		#self.prevmode = self.mode
		self.mode = 'off'
		for touch in touches:
			if touch.location in scene.Rect(*self.rect):
				self.mode = 'on'
			#elif self.prevmode == 'on':
				#self.mode = 'up'
				
#		if self.mode == 'on':
#			try:
#				self.on()
#			except AttributeError:
#				pass
#		elif self.mode == 'up':
#			try:
#				self.up()
#			except AttributeError:
#				pass
#		else:
#			try:
#				self.off()
#			except AttributeError:
#				pass

		try:
			if self.mode == 'on':
				self.on()
			else:
				self.off()
		except AttributeError:
			pass

