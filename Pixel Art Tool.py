from scene import *

class Tool (Scene):
	def setup(self):
		self.button = ''
		self.rep = 1
		self.r = 0.0
		self.g = 0.0
		self.b = 0.0
	
	def draw(self):
		
		# Draws arrows
		def arrows():
			fill(0.9, 0.9, 0.9)
			stroke_weight(0)
			
			if self.button == 'right':
				ellipse(250, 60, 60, 60)
			elif self.button == 'down':
				ellipse(200, 10, 60, 60)
			elif self.button == 'up':
				ellipse(200, 110, 60, 60)
			elif self.button == 'left':
				ellipse(150, 60, 60, 60)
			
			# Draw arrows
			stroke(0.50, 1.00, 0.00)
			stroke_weight(2)
			line(280, 70, 300, 90)
			line(300, 90, 280, 110)
			line(210, 40, 230, 20)
			line(230, 20, 250, 40)
			line(210, 140, 230, 160)
			line(230, 160, 250, 140)
			line(180, 70, 160, 90)
			line(160, 90, 180, 110)
			
		def color(x, y, color):
			fill(color[0], color[1], color[2])
			stroke(0.50, 0.50, 0.50)
			stroke_weight(1)
			rect(x, y, 20, 20)
			
		def colors():
			pass
			
		def rgb():
			tint(0, 0, 0)
			text('r:', 'AvenirNext-UltraLight', 22, 10, 110, 9)
			text('g:', 'AvenirNext-UltraLight', 22, 10, 60, 9)
			text('b:', 'AvenirNext-UltraLight', 22, 10, 10, 9)
			
			stroke(0.50, 1.00, 0.00)
			stroke_weight(0)
			fill(0.9, 0.9, 0.9)
			
			if self.button == 'r-':
				ellipse(35, 110, 30, 30)
				if self.rep == 1:
					self.r -= 0.1
					self.rep = 0
			elif self.button == 'r+':
				ellipse(95, 110, 30, 30)
				if self.rep == 1:
					self.r += 0.1
					self.rep = 0
			stroke_weight(2)
			fill(0.9, 0.9, 0.9)
			line(40, 125, 60, 125)
			line(100, 125, 120, 125)
			line(110, 115, 110, 135)
			
			stroke_weight(0)
			if self.button == 'g-':
				ellipse(35, 60, 30, 30)
				if self.rep == 1:
					self.g -= 0.1
					self.rep = 0
			elif self.button == 'g+':
				ellipse(95, 60, 30, 30)
				if self.rep == 1:
					self.g += 0.1
					self.rep = 0
			stroke_weight(2)
			fill(0.9, 0.9, 0.9)
			line(40, 75, 60, 75)
			line(100, 75, 120, 75)
			line(110, 65, 110, 85)
			
			stroke_weight(0)
			if self.button == 'b-' and self.b > 0.1:
				ellipse(35, 10, 30, 30)
				if self.rep == 1:
					self.b -= 0.1
					self.rep = 0
				if self.b == 2.77555756156e-17:
					self.b = 0.0
				print self.b
			elif self.button == 'b+' and self.b < 0.9:
				ellipse(95, 10, 30, 30)
				if self.rep == 1:
					self.b += 0.1
					self.rep = 0
			stroke_weight(2)
			fill(0.9, 0.9, 0.9)
			line(40, 25, 60, 25)
			line(100, 25, 120, 25)
			line(110, 15, 110, 35)
			
			text(str(self.r), 'AvenirNext-UltraLight', 22, 80, 110, 8)
			text(str(self.g), 'AvenirNext-UltraLight', 22, 80, 60, 8)
			text(str(self.b), 'AvenirNext-UltraLight', 22, 80, 10, 8)
			
		background(1, 1, 1)
		stroke(0, 0, 0)
		stroke_weight(1)
		line(0, 180, 320, 180)
		arrows()
		#rgb()
		color(40, 40, (0, 0, 0.7))
		
	def touch_began(self, touch):
		if touch.location in Rect(250, 60, 60, 60):
			self.button = 'right'
		elif touch.location in Rect(200, 10, 60, 60):
			self.button = 'down'
		elif touch.location in Rect(200, 110, 60, 60):
			self.button = 'up'
		elif touch.location in Rect(160, 60, 60, 60):
			self.button = 'left'
#		elif touch.location in Rect(35, 110, 30, 30):
#			self.button = 'r-'
#		elif touch.location in Rect(95, 110, 30, 30):
#			self.button = 'r+'
#		elif touch.location in Rect(35, 60, 30, 30):
#			self.button = 'g-'
#		elif touch.location in Rect(95, 60, 30, 30):
#			self.button = 'g+'
#		elif touch.location in Rect(35, 10, 30, 30):
#			self.button = 'b-'
#		elif touch.location in Rect(95, 10, 30, 30):
#			self.button = 'b+'
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		self.button = ''
		self.rep = 1

run(Tool())
