from scene import *

class Slider (Scene):
	def setup(self):
		# This will be called before the first frame is drawn.
		pass
	
	def draw(self):
		# This will be called for every frame (typically 60 times per second).
		background(1, 1, 1)
		stroke(0, 0, 1)
		stroke_weight(2)
		line(110, 240, 210, 240)
		
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		pass

run(Slider())
