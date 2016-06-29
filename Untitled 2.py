from scene import *

class MyScene (Scene):
	def setup(self):
		# This will be called before the first frame is drawn.
		pass
	
	def draw(self):
		# This will be called for every frame (typically 60 times per second).
		background(0, 0, 0)
		# Draw a red circle for every finger that touches the screen:
		fill(1, 1, 1)
		rect(20, 20, 20, 20)
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		pass

run(MyScene())
