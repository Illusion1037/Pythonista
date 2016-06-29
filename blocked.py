from scene import *
import towers

class Tile (object):
	def __init__(self, pos, type):
		self.pos = (pos[0] * 40, pos[1] * 40)
		self.type = type
		
		
	def set_tower(self, pos, type):
		pass

class BlockTD (Scene):
	def setup(self):
		# This will be called before the first frame is drawn.
		pass
	
	def draw(self):
		pass 
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		pass

run(BlockTD())
