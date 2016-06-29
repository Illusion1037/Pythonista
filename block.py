from scene import *

class Block (object):
	def __init__(self, pos):
		self.pos = pos
		self.old_pos = pos
		self.size = (20, 20)
		self.old_size = (20, 20)
		
	def draw(self):
		fill(0.00, 0.00, 0.20)
		rect(self.old_pos[0], self.old_pos[1], self.old_size[0], self.old_size[1])
		
		translate(20, 20)
		fill(0.70, 0.70, 0.70)
		rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
		
	def touching(self, platforms):
		touching = []
		for platform in platforms:
			if self.pos[1] <= platform.rect[1] and platform.rect[0] - 20 < self.pos[0] and self.pos[0] < platform.rect[2] + platform.rect[0]:
				touching.append(platform)
				return touching
			else:
				return False
		
class Platform (object):
	def __init__(self, rect, type=0):
		self.rect = rect
		self.type = type
		
	def draw(self):
		rotate(-45)
		if self.type == 0:
			fill(0.40, 1.00, 1.00)
			
		rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

class BlockGame (Scene):
	def setup(self):
		self.platforms = [Platform((0, 20, 480, 20)), Platform((0, 120, 480, 20))]
		
		self.movement = []
		self.origin = [0, 0]
		self.block_pos = [20, 40]
		self.block_xv = 0
		self.block_yv = 0
		self.jumping = False
		self.jump_h = False
		
		self.block = Block(self.block_pos)
	
	def draw(self):
		background(0.00, 0.00, 0.50)
		
		self.touching = self.block.touching(self.platforms)
		if not self.touching == False:
			for platform in self.touching:
				plat_top = platform.rect[1] + 20
			
			if self.block.pos[1] - plat_top <= self.block_yv and self.block_yv <= 1:
				self.block.pos[1] = plat_top
				self.jumping = False
				self.block_yv = 0
			
		if self.block_pos[0] < 0:
			self.block_pos[0] = 0
			self.block_xv = 0
			
		elif self.block_pos[0] > 460:
			self.block_pos[0] = 460
			self.block_xv = 0
			
		else:
			
			if 'left' in self.movement:
				self.block_xv -= 0.3
			elif 'right' in self.movement:
				self.block_xv += 0.3
			elif self.block_xv <= -1:
				self.block_xv += 1
			elif self.block_xv >= 1:
				self.block_xv -= 1
			else:
				self.block_xv = 0
				
		if 'up' in self.movement and not self.jumping:
			self.block_yv = 15
			self.jumping = True
		elif self.jumping:
			self.block_yv -= 1
		
		self.block_pos[1] += self.block_yv
		self.block_pos[0] += self.block_xv
		self.block.draw()
		
		for platform in self.platforms:
			platform.draw()
			
	def touch_began(self, touch):
		if touch.location in Rect(0, 0, 80, 320):
			self.movement.append('left')
		elif touch.location in Rect(400, 0, 80, 320):
			self.movement.append('right')
		else:
			self.movement.append('up')
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		if touch.location in Rect(0, 0, 80, 320) and 'left' in self.movement:
			self.movement.remove('left')
		elif touch.location in Rect(400, 0, 80, 320) and 'right' in self.movement:
			self.movement.remove('right')
		elif 'up' in self.movement:
			self.movement.remove('up')

run(BlockGame(), LANDSCAPE)
