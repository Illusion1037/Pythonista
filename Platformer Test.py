from scene import *

class Platformer (Scene):
	def setup(self):
		# Vars for buttons
		self.leftCol = 0.5
		self.upCol = 0.35
		self.rightCol = 0.5
		self.left = 0
		self.up = 0
		self.right = 0
		
		# Size if screen - for memory
		self.SCREENSIZE = (480, 320)
		
		# X, Y for main sprite
		self.x = 20
		self.y = 200
		
		# Vectors for main sprite
		self.v = 0
		self.jumpv = 0
		self.counter = 0
		self.startjump = 0
		self.grounded = 0
		
		# Levels
		self.lvl1 = [[0, 6, 12, 1, 1], [12, 7, 10, 1, 1]]
		
	def draw(self):
		def buttons(r1, g1, b1, r2, g2, b2, r3, g3, b3):
			fill(r1, g1, b1)
			rect(0, 0, 50, 100)
			#fill(r2, g2, b2)
			#rect(50, 0, 380, 50)
			fill(r3, g3, b3)
			rect(430, 0, 50, 100)
			stroke(1, 1, 1)
			stroke_weight(2)
			line(40, 20, 10, 50)
			line(10, 50, 40, 80)
			line(440, 20, 470, 50)
			line(470, 50, 440, 80)
			#line(200, 10, 240, 40)
			#line(240, 40, 280, 10)
			stroke_weight(0)
			
		def real(num):
			return num * 20
			
		def touching(obj, color):
			for platform in self.lvl1:
				if color == 1:
					plat = Rect(real(platform[0]), real(platform[1]), 	real(platform[2]), real(platform[3]))
			
				if obj == 'main':
					if Rect(self.x, self.y, 10, 10).intersects(plat):
						if real(platform[1]) >= self.y - 20:
							self.y += real(platform[1]) - self.y + 20
							return True
							self.grounded = 1
						if real(platform[0]) + self.v < self.x + 19 and real(platform[1]) == self.y:
							self.v = 0
							self.x -= 12
							self.right = 0
						if platform[0] == self.x - 19:
							self.x += 1
					
		
		def sprite(name):
			if name == 'main':
				fill(0, 0.75, 0)
				rect(self.x, self.y, 20, 20)
				
		def level(level):	
			for platform in level:
				if platform[4] == 1:
					fill(0, 0, 1)
				rect(real(platform[0]), real(platform[1]), real(platform[2]), real(platform[3]))
				
		background(0, 0, 0)
		
		level(self.lvl1)
		
		touching('main', 1)
		
		sprite('main')
		if self.left == 1 and self.v > -5:
			self.v -= 0.25
		if self.right == 1 and self.v < 5:
			self.v += 0.25
		if self.up == 1:
			self.jumpv = 3
			self.startjump = 1
		if self.left == 0 and self.up == 0 and self.right == 0:
			if self.v > 0:
				self.v -= 0.25
			elif self.v < 0:
				self.v += 0.25
		if self.counter != 30 and self.startjump == 1:
			self.jumpv -= 0.1
			self.counter += 1
		else:
			self.counter = 0
			self.jumpv = 0
			self.up = 0
			self.startjump = 0
		self.x += self.v
		self.y += self.jumpv
		
		if not self.grounded:
			self.jumpv -= 3
			self.y += self.jumpv
		
		# Draw buttons
		buttons(0, 0, self.leftCol, 0, 0, self.upCol, 0, 0, self.rightCol)
	
	def touch_began(self, touch):
		if Rect(touch.location[0], touch.location[1], 1, 1).intersects(Rect(0, 0, 50, 100)):
			self.leftCol = 0
			self.left = 1
		elif Rect(touch.location[0], touch.location[1], 1, 1).intersects(Rect(430, 0, 50, 100)):
			self.rightCol = 0
			self.right = 1
			
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		if Rect(touch.location[0], touch.location[1], 1, 1).intersects(Rect(0, 0, 50, 100)):
			self.leftCol = 0.5
			self.left = 0
		#elif Rect(touch.location[0], touch.location[1], 1, 1).intersects(Rect(50, 0, 380, 50)):
			#self.upCol = 0.35
			#self.up = 0
		elif Rect(touch.location[0], touch.location[1], 1, 1).intersects(Rect(430, 0, 50, 100)):
			self.rightCol = 0.5
			self.right = 0

run(Platformer(), LANDSCAPE)
