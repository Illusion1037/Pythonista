class xyzPoint (object):
	def __init__(self, x, y, z):
		self.pos = (x, y, z)
		
	def get(self):
		return self.pos
		
	def x(self):
		return self.pos[0]
		
	def y(self):
		return self.pos[1]
		
	def z(self):
		return self.pos[2]
		
	def rasterize(self, cameraPoint):
		SCREENW = 480
		SCREENH = 320
		
		x = self.x()
		y = self.y()
		z = self.z()
		
		cx = cameraPoint.x() - x
		cy = cameraPoint.y() - y
		cz = cameraPoint.z() - z
		
		newx = (cx / cz)
		newy = (cy / cz)
		
#		ASPECT = SCREENW / SCREENH
#		
#		if ASPECT > 1:
#			newx /= ASPECT
#		else:
#			newy *= ASPECT
		
		return xyPoint(newx, newy)
		
class xyPoint (object):
	def __init__(self, x, y):
		self.pos = (x, y)
		
	def get(self):
		return self.pos
		
	def x(self):
		return self.pos[0]
		
	def y(self):
		return self.pos[1]
