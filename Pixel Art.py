from scene import *

class PixelArt (Scene):
	def setup(self):
		self.xvals = [10]
		self.yvals = [10]
	
	def draw(self):
		# This will be called for every frame (typically 60 times per second).
		background(0, 0, 0)
		# Draw a red circle for every finger that touches the screen:
		fill(1, 0, 0)
		for touch in self.touches.values():
			rect(round((touch.location.x - 50) / 10) * 10, round((touch.location.y - 50) / 10) * 10, 10, 10)
			self.xvals.append(round((touch.location.x - 50) / 10) * 10)
			self.yvals.append(round((touch.location.y - 50) / 10) * 10)
		
		for val in self.xvals:
			rect(self.xvals[int(val)], self.yvals[int(val)], 10, 10)
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		pass

run(PixelArt())
