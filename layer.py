import scene

class Layer (object):
	def __init__(self):
		self.trans = (0, 0)
		self.rot = 0
		self.scl = (1, 1)
		
	def draw(self):
		try:
			scene.push_matrix()
			self.transform()
			scene.translate(*self.trans)
			scene.rotate(self.rot)
			scene.scale(*self.scl)
			self.main()
			scene.pop_matrix()
		except AttributeError:
			pass
			
	def translate(self, pos):
		self.trans = pos
	
	def rotate(self, deg):
		self.rot = deg
		
	def scale(self, x, y):
		self.scl = (x, y)
		
