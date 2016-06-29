from scene import *

class Tower (object):
	def __init__(self, rect):
		self.x = rect[0]
		self.y = rect[1]
		self.w = rect[2]
		self.h = rect[3]
		
	def set_rect(self, rect):
		self.x = rect[0]
		self.y = rect[1]
		self.w = rect[2]
		self.h = rect[3]
		
	def get_rect(self):
		return Rect(self.x, self.y, self.w, self.h)
		
class FixedRifle (Tower):
	def __init__(self, pos, files):
		self.x = pos[0]
		self.y = pos[1]
		
		self.w = self.h = 20
		
		self.map_norm = []
		self.map_firing = []
		
		f = open('FixedRifle_norm.txt', 'r')
		
		for line in f:
			self.map_norm.append(line)
			
		f.close()
		
	def draw(self):
		for row in range(20):
			for col in range(20):
				tile = self.map_norm[19 - row][col]
				
				if tile == 'B':
					fill(0, 0, 0)
				elif tile == 'L':
					fill(0.7, 0.7, 0.7)
				elif tile == 'G':
					fill(0.5, 0.5, 0.5)
				elif tile == 'D':
					fill(0.3, 0.3, 0.3)
				elif tile == 'R':
					fill(1, 0, 0)
				elif tile == 'Y':
					fill(1, 1, 0)
				else:
					fill(1, 1, 1)
				
				x = self.x + col * 2
				y = self.y + row * 2
				
				rect(x, y, 2, 2)
				
class Test (Scene):
	def setup(self):
		self.tower = FixedRifle((20, 20), ('FixedRifle_norm.txt'))
		
	def draw(self):
		background(1, 1, 1)
		self.tower.draw()
		
run(Test())
