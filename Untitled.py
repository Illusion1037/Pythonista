import easymod

class Test (object):
	def init(self):
		self.a = 0
		print 'initialized'
		
	def run(self):
		print self.a
		self.a += 1
		
easymod.run(Test())
