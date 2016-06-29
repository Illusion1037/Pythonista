from scene import *
import xyz

class MyScene (Scene):
	def setup(self):
		self.cube = (xyz.xyzPoint(50, 50, 50), xyz.xyzPoint(-50, 50, 50), xyz.xyzPoint(50, -50, 50), xyz.xyzPoint(-50, -50, 50), xyz.xyzPoint(50, 50, -50), xyz.xyzPoint(-50, 50, -50), xyz.xyzPoint(50, -50, -50), xyz.xyzPoint(-50, -50, -50))
		
	def pointline(self, point1, point2):
		line(self.cube[point1].rasterize(xyz.xyzPoint(0, 0, -200)).x(), self.cube[point1].rasterize(xyz.xyzPoint(0, 0, -200)).y(), self.cube[point2].rasterize(xyz.xyzPoint(0, 0, -200)).x(), self.cube[point2].rasterize(xyz.xyzPoint(0, 0, -200)).y())
		
		print(self.cube[point1].rasterize(xyz.xyzPoint(0, 0, -200)).x(), self.cube[point1].rasterize(xyz.xyzPoint(0, 0, -200)).y(), self.cube[point2].rasterize(xyz.xyzPoint(0, 0, -200)).x(), self.cube[point2].rasterize(xyz.xyzPoint(0, 0, -200)).y())
	
	def draw(self):
		background(0, 0, 0)
		stroke(0, 0, 1)
		stroke_weight(2)
		self.pointline(0, 1)
		self.pointline(1, 2)
		self.pointline(2, 3)
		self.pointline(3, 0)
		self.pointline(0, 4)
		self.pointline(1, 5)
		self.pointline(2, 6)
		self.pointline(3, 7)
		self.pointline(4, 5)
		self.pointline(5, 6)
		self.pointline(6, 7)
		self.pointline(7, 4)
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		pass

run(MyScene())
